from bitstring import BitStream
from input_action import InputAction
from input_action.types import InputActionType
from network_message.payloads import ClientToServerHeartbeatPayload, MessagePayload, ServerToClientHeartbeatPayload, TransferBlockPayload, TransferBlockRequestPayload
from network_message.types import MessageType
from utils import pretty_stringify_object


class NetworkMessage:
    last_fragment: bool
    fragmented: bool
    random: bool
    network_message_type: MessageType
    message_payload: MessagePayload

    def __init__(self, last_fragment: bool, fragmented: bool, random: bool, network_message_type: MessageType, message_payload: MessagePayload) -> None:
        self.last_fragment = last_fragment
        self. fragmented = fragmented
        self.random = random
        self.network_message_type = network_message_type
        self.message_payload = message_payload

    @classmethod
    def from_bitstream(cls, bit_stream: BitStream):
        last_fragment, fragmented, random, message_type = bit_stream.readlist(
            "bool, bool, bool, uint5")
        message_type = MessageType(message_type)
        if fragmented:
            raise NotImplementedError(
                "Decoding of fragmented network messages not implemented.")
        payload = cls.decode_message_payload(message_type, bit_stream)
        return cls(last_fragment, fragmented, random, message_type, payload)

    @classmethod
    def decode_message_payload(cls, message_type: MessageType, bit_stream: BitStream) -> MessagePayload:
        match message_type:
            case MessageType.ClientToServerHeartbeat:
                return ClientToServerHeartbeatPayload.from_bitstream(bit_stream)
            case MessageType.ServerToClientHeartbeat:
                return ServerToClientHeartbeatPayload.from_bitstream(bit_stream)
            case MessageType.TransferBlockRequest:
                return TransferBlockRequestPayload.from_bitstream(bit_stream)
            case MessageType.TransferBlock:
                return TransferBlockPayload.from_bitstream(bit_stream)
            case _:
                raise NotImplementedError(f"Unsupported MessageType: {message_type}")

    def to_bitstream(self) -> BitStream:
        return_stream = BitStream(f"bool={self.last_fragment}, bool={self.fragmented}, bool={
                                  self.random}, uint5={self.network_message_type.value}")
        return_stream += self.message_payload.to_bitstream()
        return return_stream

    def inject_input_action(self, input_action: InputAction) -> None:
        self.message_payload.tick_closures[0].input_actions.append(
            input_action)
        
    def filter_input_action_type(self, input_action_type: InputActionType) -> None:
        for tick_closure in self.message_payload.tick_closures:
            for input_action in tick_closure.input_actions:
                if input_action.input_action_type == input_action_type:
                    tick_closure.input_actions.remove(input_action)
        if not any([len(tick_closure.input_actions) > 0 for tick_closure in self.message_payload.tick_closures]):
            self.message_payload.all_tick_closures_are_empty = True
        
    def __str__(self):
        return pretty_stringify_object(self)
