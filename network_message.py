from bitstring import BitStream
from input_action import InputAction
from input_action_payload import StopWalkingPayload
from input_action_type import InputActionType
from message_payload import ClientToServerHeartbeatPayload, MessagePayload, ServerToClientHeartbeatPayload, TransferBlockPayload, TransferBlockRequestPayload
from message_type import MessageType


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
        last_fragment, fragmented, random, message_type = bit_stream.readlist("bool, bool, bool, uint5")
        message_type = MessageType(message_type)
        if fragmented: raise NotImplementedError("Decoding of fragmented network messages not implemented.")
        payload = cls.decode_message_payload(message_type, bit_stream)
        return cls(last_fragment, fragmented, random, message_type, payload)

    @classmethod
    def decode_message_payload(cls, message_type: MessageType, bit_stream: BitStream) -> MessagePayload:
        match message_type:
            case MessageType.Ping:
                raise NotImplementedError(f"Decoding of MessageType {message_type}-Payload not implemented.")
            case MessageType.PingReply:
                raise NotImplementedError(f"Decoding of MessageType {message_type}-Payload not implemented.")
            case MessageType.ConnectionRequest:
                raise NotImplementedError(f"Decoding of MessageType {message_type}-Payload not implemented.")
            case MessageType.ConnectionRequestReply:
                raise NotImplementedError(f"Decoding of MessageType {message_type}-Payload not implemented.")
            case MessageType.ConnectionRequestReplyConfirm:
                raise NotImplementedError(f"Decoding of MessageType {message_type}-Payload not implemented.")
            case MessageType.ConnectionAcceptOrDeny:
                raise NotImplementedError(f"Decoding of MessageType {message_type}-Payload not implemented.")
            case MessageType.ClientToServerHeartbeat:
                return ClientToServerHeartbeatPayload.from_bitstream(bit_stream)
            case MessageType.ServerToClientHeartbeat:
                return ServerToClientHeartbeatPayload.from_bitstream(bit_stream)
            case MessageType.GetOwnAddress:
                raise NotImplementedError(f"Decoding of MessageType {message_type}-Payload not implemented.")
            case MessageType.GetOwnAddressReply:
                raise NotImplementedError(f"Decoding of MessageType {message_type}-Payload not implemented.")
            case MessageType.NatPunchRequest:
                raise NotImplementedError(f"Decoding of MessageType {message_type}-Payload not implemented.")
            case MessageType.NatPunch:
                raise NotImplementedError(f"Decoding of MessageType {message_type}-Payload not implemented.")
            case MessageType.TransferBlockRequest:
                return TransferBlockRequestPayload.from_bitstream(bit_stream)
            case MessageType.TransferBlock:
                return TransferBlockPayload.from_bitstream(bit_stream)
            case MessageType.RequestForHeartbeatWhenDisconnecting:
                raise NotImplementedError(f"Decoding of MessageType {message_type}-Payload not implemented.")
            case MessageType.LANBroadcast:
                raise NotImplementedError(f"Decoding of MessageType {message_type}-Payload not implemented.")
            case MessageType.GameInformationRequest:
                raise NotImplementedError(f"Decoding of MessageType {message_type}-Payload not implemented.")
            case MessageType.GameInformationRequestReply:
                raise NotImplementedError(f"Decoding of MessageType {message_type}-Payload not implemented.")
            case MessageType.Empty:
                raise NotImplementedError(f"Decoding of MessageType {message_type}-Payload not implemented.")
            case _:
                raise TypeError(f"Unsupported MessageType: {message_type}")
            
    def to_bitstream(self) -> BitStream:
        return_stream = BitStream(f"bool={self.last_fragment}, bool={self.fragmented}, bool={self.random}, uint5={self.network_message_type.value}")
        return_stream += self.message_payload.to_bitstream()
        return return_stream
    
    def inject_input_action(self, input_action: InputAction) -> None:
        if not self.network_message_type == MessageType.ClientToServerHeartbeat:
            raise NotImplementedError("Injection only implemented for client to server heartbeat.")
        if not self.message_payload.has_tick_closures:
            raise NotImplementedError("Can only inject into messages that have tick closures.")
        if self.message_payload.all_tick_closures_are_empty:
            raise NotImplementedError("Can only inject into non empty tick closures")
        self.message_payload.tick_closures[0].input_actions.append(input_action)


if __name__ == "__main__":
    example_input = BitStream(bytes.fromhex("26061372502da0370000023d010289370000"))
    example_network_message = NetworkMessage.from_bitstream(example_input)
    
    example_input_action = InputAction(InputActionType.StopWalking, StopWalkingPayload(0))
    example_network_message.inject_input_action(example_input_action)
    example_output = example_network_message.to_bitstream()
    assert example_input != example_output
