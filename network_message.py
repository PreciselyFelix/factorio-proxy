from bitstring import BitStream
from message_payload import MessagePayload, ServerToClientHeartbeatPayload, TransferBlockPayload, TransferBlockRequestPayload
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
                raise NotImplementedError(f"Decoding of MessageType {message_type}-Payload not implemented.")
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


if __name__ == "__main__":
    example_bitstream = BitStream(bytes.fromhex("0d060000009c91b72f53d3782e3b33abdebe42e9c9c24805fda5debf4a4dd30a0197fc1ab506de3293fbfbbe4e0d76907a81e713a8c5a6cb58c5900e279c4c0b87b3d3a5ca44ae891689b8cfd826958ea5fa62f64066345f1a2fd2c2b1626e0a23f873d43a3c810984e6e894cf53cb74218f210a7e0baa2fd0a2d244e1c048e1804dfa222d1ac98de6a630780cd4b3d43e82e15ccc0e970b36f1396a1bc1c82e16667dc02fd152000e8fcbe8152ca51ca6c064a19cfb212df33ba7cc0065196592f90b505a989ecd4c67416da65c284ca46229a7500ba67b00e4545a1c99c8900b931e754552f53c3e91166088b652dd349a5298782bb5942a4393d9e1718cfb0c72de468bcad9a9fd18f036e9edb47826379e1fc6dc0fa43e416d02181c2fefa0857aa8bf1364623c65cb188132299ea45635e03213d9cad4f078aef8143507cbbe8bba7cce1cc88e49eff034790fad084ce208924cef7bab66f7bdaf6a76fffbab660f7c809aa4916a027e906a98b78f52f38142612487b1328eaef7a851d41f79495113fa2e37a1b2165033985ccc4288319a1a6ac1e8992ab1b8cb0ce526cab5b478147d9d09a7d6894428e64aa548c6425a0461942b8e89e8110cf5d42918a2e90db414d3427044b31aa9be343d912f634234515a4a9bf766910f52ca24a5a96ea28059546ca12681556fadd462f0ab8445d43a542962fdc02a"))
    example_network_message = NetworkMessage.from_bitstream(example_bitstream)
    print(example_network_message)
    print(example_network_message.network_message_type)
    print(example_network_message.message_payload)
