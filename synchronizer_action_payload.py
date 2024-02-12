from abc import ABC, abstractmethod, abstractclassmethod
from typing import Optional

from bitstring import BitStream


class SynchronizerActionPayload(ABC):
    @abstractclassmethod
    def from_bitstream(cls, bit_stream: BitStream):
        pass

    @abstractmethod
    def to_bitstream(self) -> BitStream:
        pass

class MapDownloadingProgressUpdatePayload(SynchronizerActionPayload):
    progress: int
    sender_peer_id: int | None

    def __init__(self, progress: int, sender_peer_id: Optional[int] = None) -> None:
        self.progress = progress
        self.sender_peer_id = sender_peer_id

    @classmethod
    def from_bitstream(cls, bit_stream: BitStream, has_sender_peer_id: bool):
        progress = bit_stream.read("uintle8")
        if has_sender_peer_id:
            sender_peer_id = bit_stream.read("uintle16")
            return cls(progress, sender_peer_id)
        else:
            return cls(progress)
    
    def to_bitstream(self) -> BitStream:
        return_bitstream = BitStream(f"uintle8={self.progress}")
        if self.sender_peer_id is not None:
            return_bitstream += BitStream(f"uintle16={self.sender_peer_id}")
        return return_bitstream
