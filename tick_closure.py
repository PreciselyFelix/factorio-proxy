from typing import List

from bitstring import BitStream

from input_action import InputAction


class TickClosure:
    update_tick = int
    input_actions = List[InputAction]

    def __init__(self, update_tick: int, input_actions: List[InputAction]) -> None:
        self.update_tick = update_tick

    @classmethod
    def from_bitstream(cls, bit_stream: BitStream, all_tick_closures_are_empty):
        update_tick = bit_stream.read("uintle32")
        input_actions = []
        if not all_tick_closures_are_empty:
            amount_of_input_actions = bit_stream.read("uintle8") // 2
            for i in range(amount_of_input_actions):
                input_actions.append(InputAction.from_bitstream(bit_stream))
        return cls(update_tick, input_actions)
    
    def to_bitstream(self) -> BitStream:
        return_stream = BitStream(f"uintle32={self.update_tick}")
        return return_stream
