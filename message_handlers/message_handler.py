from abc import ABC, abstractmethod

class MessageHandler(ABC):
    @abstractmethod
    def handle_message(self, message_data: bytes) -> bytes:
        pass