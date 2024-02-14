from abc import ABC, abstractmethod

from bitstring import BitStream

from utils.direction import Direction
from utils import pretty_stringify_object


class InputActionPayload(ABC):
    @classmethod
    @abstractmethod
    def from_bitstream(cls, bit_stream: BitStream):
        pass

    @abstractmethod
    def to_bitstream(self) -> BitStream:
        pass

    def __str__(self) -> str:
        return pretty_stringify_object(self)

class CheckCRCHeuristicPayload(InputActionPayload):
    crc: int
    tick_of_crc: int

    def __init__(self, crc: int, tick_of_crc: int) -> None:
        self.crc = crc
        self.tick_of_crc = tick_of_crc

    @classmethod
    def from_bitstream(cls, bit_stream: BitStream):
        crc, tick_of_crc = bit_stream.readlist(
            "uintle32, uintle32")

        return cls(crc, tick_of_crc)

    def to_bitstream(self) -> BitStream:
        return_stream = BitStream(f"uintle32={self.crc}, uintle32={self.tick_of_crc}")
        return return_stream


class StartWalkingPayload(InputActionPayload):
    direction: Direction

    def __init__(self, direction: Direction) -> None:
        self.direction = direction

    @classmethod
    def from_bitstream(cls, bit_stream: BitStream):
        direction_id = bit_stream.read("uintle8")
        direction = Direction(direction_id)
        return cls(direction)

    def to_bitstream(self) -> BitStream:
        return_stream = BitStream(f"uintle8={self.direction.value}")
        return return_stream


class EmptyPayload(InputActionPayload):
    def __init__(self) -> None:
        return

    @classmethod
    def from_bitstream(cls, bit_stream: BitStream):
        return cls()

    def to_bitstream(self) -> BitStream:
        return BitStream()
    
    
class RotateEntityPayload(InputActionPayload):
    data: int

    def __init__(self, data: int) -> None:
        self.data = data

    @classmethod
    def from_bitstream(cls, bit_stream: BitStream):
        data = bit_stream.read("uintle8")
        return cls(data)
    
    def to_bitstream(self) -> BitStream:
        return_stream = BitStream(f"uintle8={self.data}")
        return return_stream