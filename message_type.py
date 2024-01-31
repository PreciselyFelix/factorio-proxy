from enum import Enum

class MessageType(Enum):
    Ping = 0
    PingReply = 1
    ConnectionRequest = 2
    ConnectionRequestReply = 3
    ConnectionRequestReplyConfirm = 4
    ConnectionAcceptOrDeny = 5
    ClientToServerHeartbeat = 6
    ServerToClientHeartbeat = 7
    GetOwnAddress = 8
    GetOwnAddressReply = 9
    NatPunchRequest = 10
    NatPunch = 11
    TransferBlockRequest = 12
    TransferBlock = 13
    RequestForHeartbeatWhenDisconnecting = 14
    LANBroadcast = 15
    GameInformationRequest = 16
    GameInformationRequestReply = 17
    Empty = 18
