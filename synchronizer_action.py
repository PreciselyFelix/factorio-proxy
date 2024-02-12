from bitstring import BitStream
from synchronizer_action_payload import MapDownloadingProgressUpdatePayload, SynchronizerActionPayload
from synchronizer_action_type import SynchronizerActionType


class SynchronizerAction:
    synchronizer_action_type: SynchronizerActionType
    synchronizer_action_payload: SynchronizerActionPayload
    is_server_to_client_heartbeat: bool

    def __init__(self, synchronizer_action_type: SynchronizerActionType, synchronizer_action_payload: SynchronizerActionPayload, is_server_to_client_heartbeat: bool) -> None:
        self.synchronizer_action_type = synchronizer_action_type
        self.synchronizer_action_payload = synchronizer_action_payload
        self.is_server_to_client_heartbeat = is_server_to_client_heartbeat

    @classmethod
    def from_bitstream(cls, bit_stream: BitStream, is_server_to_client_heartbeat: bool):
        synchronizer_action_type = SynchronizerActionType(bit_stream.read("uintle8"))
        synchronizer_action_payload = cls.decode_synchronizer_action_payload(synchronizer_action_type, bit_stream, is_server_to_client_heartbeat)
        return cls(synchronizer_action_type, synchronizer_action_payload, is_server_to_client_heartbeat)
    
    @classmethod
    def decode_synchronizer_action_payload(cls, synchronizer_action_type: SynchronizerActionType, bit_stream: BitStream, is_server_to_client_heartbeat: bool) -> SynchronizerActionPayload:
        match synchronizer_action_type:
            case SynchronizerActionType.MapDownloadingProgressUpdate:
                return MapDownloadingProgressUpdatePayload.from_bitstream(bit_stream,is_server_to_client_heartbeat)
            case _:
                raise NotImplementedError(f"Unsupported synchronizer action type: {synchronizer_action_type}")
            
    def to_bitstream(self) -> BitStream:
        return_stream = BitStream(f"uintle8={self.synchronizer_action_type.value}")
        return_stream += self.synchronizer_action_payload.to_bitstream()
        return return_stream