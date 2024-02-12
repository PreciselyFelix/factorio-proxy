from bitstring import BitStream
from input_action_payload import CheckCRCHeuristicPayload, InputActionPayload, StartWalkingPayload, StopWalkingPayload
from input_action_type import InputActionType


class InputAction:
    input_action_type = InputActionType
    input_action_payload = InputActionPayload

    def __init__(self, input_action_type: InputActionType, input_action_payload: InputActionPayload) -> None:
        self.input_action_type = input_action_type
        self.input_action_payload = input_action_payload

    @classmethod
    def from_bitstream(cls, bit_stream: BitStream):
        input_action_type = InputActionType(bit_stream.read("uintle8"))
        input_action_payload = cls.decode_input_action(input_action_type, bit_stream)

        return cls(input_action_type, input_action_payload)
    
    @classmethod
    def decode_input_action(cls, input_action_type: InputActionType, bit_stream: BitStream) -> InputActionPayload:
        match input_action_type:
            case InputActionType.StartWalking:
                return StartWalkingPayload.from_bitstream(bit_stream)
            case InputActionType.StopWalking:
                return StopWalkingPayload.from_bitstream(bit_stream)
            case InputActionType.CheckCRCHeuristic:
                return CheckCRCHeuristicPayload.from_bitstream(bit_stream)
            case _:
                raise NotImplementedError(f"Decoding of InputActionType {input_action_type}-Payload not implemented.")

    def to_bitstream(self) -> BitStream:
        return_stream = BitStream(f"uintle8={self.input_action_type.value}")
        return_stream += self.input_action_payload.to_bitstream()
        return return_stream