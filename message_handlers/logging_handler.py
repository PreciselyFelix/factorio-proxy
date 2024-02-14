from network_message import NetworkMessage
from message_handlers import MessageHandler
from bitstring import BitStream
from _logging import FACTORIO_LOGGER, ErrorLogWriter, setup_logging

class LoggingHandler(MessageHandler):
    def __init__(self) -> None:
        setup_logging()

    def handle_message(self, message_data: bytes) -> bytes:
        try:
            network_message = NetworkMessage.from_bitstream(BitStream(message_data))
            FACTORIO_LOGGER.debug(network_message)
            reconstructed_data = network_message.to_bitstream().tobytes()
        except NotImplementedError as e:
            FACTORIO_LOGGER.info(f"Decoding of message not implemented: {e}")
            return message_data
        except Exception as e:
            FACTORIO_LOGGER.exception(f"Could not deconstruct network message: {e}")
            return message_data
        
        if not reconstructed_data == message_data:
            FACTORIO_LOGGER.warning("Reconstruction differs from original:")
            FACTORIO_LOGGER.warning("original message:")
            BitStream(message_data).pp(stream=ErrorLogWriter)
            FACTORIO_LOGGER.warning("reconstructed message:")
            BitStream(reconstructed_data).pp(stream=ErrorLogWriter)
            FACTORIO_LOGGER.warning(network_message)
            return message_data
        else:
            return reconstructed_data