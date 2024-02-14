from .message_handler import MessageHandler


class PassThroughHandler(MessageHandler):
    def handle_message(self, message_data: bytes) -> bytes:
        return message_data