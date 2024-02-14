from bitstring import BitStream
from input_action.payloads import CheckCRCHeuristicPayload, EmptyPayload, InputActionPayload, StartWalkingPayload, RotateEntityPayload
from input_action.types import InputActionType
from utils import pretty_stringify_object


class InputAction:
    input_action_type: InputActionType
    player_index: int
    input_action_payload: InputActionPayload

    def __init__(self, input_action_type: InputActionType, player_index: int, input_action_payload: InputActionPayload) -> None:
        self.input_action_type = input_action_type
        self.player_index = player_index
        self.input_action_payload = input_action_payload

    @classmethod
    def from_bitstream(cls, bit_stream: BitStream):
        input_action_type = InputActionType(bit_stream.read("uintle8"))
        player_index = bit_stream.read("uintle8")
        input_action_payload = cls.decode_input_action(
            input_action_type, bit_stream)

        return cls(input_action_type, player_index, input_action_payload)

    @classmethod
    def decode_input_action(cls, input_action_type: InputActionType, bit_stream: BitStream) -> InputActionPayload:
        match input_action_type:
            case InputActionType.StopWalking:
                return EmptyPayload.from_bitstream(bit_stream)
            case InputActionType.BeginMining:
                return EmptyPayload.from_bitstream(bit_stream)
            case InputActionType.StopMining:
                return EmptyPayload.from_bitstream(bit_stream)
            case InputActionType.ClearCursor:
                return EmptyPayload.from_bitstream(bit_stream)
            case InputActionType.OpenGui:
                return EmptyPayload.from_bitstream(bit_stream)
            case InputActionType.CloseGui:
                return EmptyPayload.from_bitstream(bit_stream)
            case InputActionType.StartWalking:
                return StartWalkingPayload.from_bitstream(bit_stream)
            case InputActionType.CheckCRCHeuristic:
                return CheckCRCHeuristicPayload.from_bitstream(bit_stream)
            case InputActionType.RotateEntity:
                return RotateEntityPayload.from_bitstream(bit_stream)
            case _:
                raise NotImplementedError(f"Unsupported input action type: {input_action_type}")

    def to_bitstream(self) -> BitStream:
        return_stream = BitStream(f"uintle8={self.input_action_type.value}")
        return_stream += BitStream(f"uintle8={self.player_index}")
        return_stream += self.input_action_payload.to_bitstream()
        return return_stream
    
    def __str__(self) -> str:
        return pretty_stringify_object(self)
