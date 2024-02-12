from abc import ABC, abstractclassmethod, abstractmethod

from bitstring import BitStream

class InputActionPayload(ABC):
    @abstractclassmethod
    def from_bitstream(cls, bit_stream: BitStream):
        pass

    @abstractmethod
    def to_bitstream(self) -> BitStream:
        pass

