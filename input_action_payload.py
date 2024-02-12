from abc import ABC, abstractclassmethod, abstractmethod

from bitstring import BitStream

from direction import Direction


class InputActionPayload(ABC):
    player_index: int

    @abstractclassmethod
    def from_bitstream(cls, bit_stream: BitStream):
        pass

    @abstractmethod
    def to_bitstream(self) -> BitStream:
        pass


class CheckCRCHeuristicPayload(InputActionPayload):
    crc = int
    tick_of_crc = int

    def __init__(self, player_index: int, crc: int, tick_of_crc: int) -> None:
        self.player_index = player_index
        self.crc = crc
        self.tick_of_crc = tick_of_crc

    @classmethod
    def from_bitstream(cls, bit_stream: BitStream):
        player_index, crc, tick_of_crc = bit_stream.readlist(
            "uintle8, uintle32, uintle32")

        return cls(player_index, crc, tick_of_crc)

    def to_bitstream(self) -> BitStream:
        return_stream = BitStream(f"uintle8={self.player_index}, uintle32={
                                  self.crc}, uintle32={self.tick_of_crc}")
        return return_stream


class StartWalkingPayload(InputActionPayload):
    direction: Direction

    def __init__(self, player_index: int, direction: Direction) -> None:
        self.player_index = player_index
        self.direction = direction

    @classmethod
    def from_bitstream(cls, bit_stream: BitStream):
        player_index, direction_id = bit_stream.readlist("uintle8, uintle8")
        direction = Direction(direction_id)
        return cls(player_index, direction)

    def to_bitstream(self) -> BitStream:
        return_stream = BitStream(f"uintle8={self.player_index}, uintle8={
                                  self.direction.value}")
        return return_stream


class StopWalkingPayload(InputActionPayload):
    def __init__(self, player_index: int) -> None:
        self.player_index = player_index

    @classmethod
    def from_bitstream(cls, bit_stream: BitStream):
        player_index = bit_stream.read("uint8")
        return cls(player_index)

    def to_bitstream(self) -> BitStream:
        return_stream = BitStream(f"uintle8={self.player_index}")
        return return_stream
