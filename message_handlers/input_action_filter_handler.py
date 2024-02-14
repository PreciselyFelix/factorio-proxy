from input_action.types import InputActionType
from message_handlers import MessageHandler
from network_message import NetworkMessage
from network_message.types import MessageType
from bitstring import BitStream
from _logging import FACTORIO_LOGGER, ErrorLogWriter, setup_logging



class InputActionFilterHandler(MessageHandler):
    filter_action_type: InputActionType
    filter_message_type: MessageType

    def __init__(
            self,
            filter_action_type: InputActionType,
            filter_message_type: MessageType
    ) -> None:
        self.filter_action_type = filter_action_type
        self.filter_message_type = filter_message_type
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
            FACTORIO_LOGGER.error("Reconstruction differs from original:")
            FACTORIO_LOGGER.error("original message:")
            BitStream(message_data).pp(stream=ErrorLogWriter)
            FACTORIO_LOGGER.error("reconstructed message:")
            BitStream(reconstructed_data).pp(stream=ErrorLogWriter)
            FACTORIO_LOGGER.error(network_message)
            return message_data
        if network_message.network_message_type == self.filter_message_type and network_message.message_payload.has_tick_closures and not network_message.message_payload.all_tick_closures_are_empty:
            network_message.filter_input_action_type(self.filter_action_type)
            modified_data = network_message.to_bitstream().tobytes()
            return modified_data
        return reconstructed_data