import atexit
import json
import socket
import logging.config
from bitstring import BitStream
from input_action import InputAction
from input_action_payload import EmptyPayload
from input_action_type import InputActionType
from message_type import MessageType

from network_message import NetworkMessage

PROXY_INPUT_PORT = 1234
FACTORIO_SERVER_PORT = 34197

PROXY_IP = "127.0.0.1"
FACTORIO_SERVER_IP = "127.0.0.1"

LOGGER = logging.getLogger("FactorioProxy")


def setup_logging() -> None:
    with open("logger_config.json") as f:
        config = json.load(f)
    logging.config.dictConfig(config)
    queue_handler = logging.getHandlerByName("queue_handler")
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)


if __name__ == "__main__":
    setup_logging()
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as proxy_socket:
        proxy_socket.bind((PROXY_IP, PROXY_INPUT_PORT))

        server_address = (FACTORIO_SERVER_IP, FACTORIO_SERVER_PORT)
        client_address = None

        while True:
            original_data, address = proxy_socket.recvfrom(1024)
            try:
                network_message = NetworkMessage.from_bitstream(
                    BitStream(original_data))
                reconstructed_data = network_message.to_bitstream()
                reconstructed_data = reconstructed_data.tobytes()
                if not reconstructed_data == original_data:
                    LOGGER.error("Reconstruction differs from original")
                    LOGGER.error(f"Original Message     : {original_data}")
                    LOGGER.error(f"Reconstructed Message: {
                                 reconstructed_data}")
                    reconstructed_data = original_data
                else:
                    try:
                        if network_message.network_message_type == MessageType.ClientToServerHeartbeat and network_message.message_payload.has_tick_closures and not network_message.message_payload.all_tick_closures_are_empty:
                            network_message.inject_input_action(InputAction(
                                InputActionType.ClearCursor, 0, EmptyPayload()))
                            reconstructed_data = network_message.to_bitstream()
                            reconstructed_data = reconstructed_data.tobytes()
                    except NotImplementedError as e:
                        LOGGER.debug(
                            f"Decoding of message not implemented: {e}")
                    except Exception as e:
                        LOGGER.error(f"Error during injection: {type(e)}, {e}")
            except NotImplementedError as e:
                LOGGER.debug(f"Decoding of message not implemented: {e}")
                reconstructed_data = original_data
            except Exception as e:
                LOGGER.error(
                    f"Error during construction of network message: {e}")
                LOGGER.error(f"Original Message     : {original_data}")
                reconstructed_data = original_data
            if address != server_address:
                client_address = address
                proxy_socket.sendto(reconstructed_data, server_address)
            elif address == server_address and client_address is not None:
                proxy_socket.sendto(reconstructed_data, client_address)
