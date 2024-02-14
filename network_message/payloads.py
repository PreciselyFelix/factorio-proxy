from abc import ABC, abstractmethod
from typing import List

from bitstring import BitStream
from synchronizer_action import SynchronizerAction

from tick_closure import TickClosure
from utils import pretty_stringify_object


class MessagePayload(ABC):
    @classmethod
    @abstractmethod
    def from_bitstream(cls, bit_stream: BitStream):
        pass

    @abstractmethod
    def to_bitstream(self) -> BitStream:
        pass

    def __str__(self) -> str:
        return pretty_stringify_object(self)


class TransferBlockRequestPayload(MessagePayload):
    block_number: int

    def __init__(self, block_number: int) -> None:
        self.block_number = block_number

    @classmethod
    def from_bitstream(cls, bit_stream: BitStream):
        block_number = bit_stream.read("uintle32")
        return cls(block_number)

    def to_bitstream(self) -> BitStream:
        return BitStream(f"uintle32={self.block_number}")
    
    def __str__(self) -> str:
        return super().__str__()


class TransferBlockPayload(MessagePayload):
    block_number: int
    data = bytes

    def __init__(self, block_number: int, data: bytes) -> None:
        self.block_number = block_number
        self.data = data

    @classmethod
    def from_bitstream(cls, bit_stream: BitStream):
        block_number = bit_stream.read("uintle32")
        data = bit_stream[bit_stream.pos:].tobytes()
        return cls(block_number, data)

    def to_bitstream(self) -> BitStream:
        return_stream = BitStream(f"uintle32={self.block_number}")
        return_stream += BitStream(self.data)
        return return_stream
    
    def __str__(self) -> str:
        return super().__str__()


class ServerToClientHeartbeatPayload(MessagePayload):
    has_synchronizer_action: bool
    all_tick_closures_are_empty: bool
    has_single_tick_closure: bool
    has_tick_closures: bool
    has_heartbeat_requests: bool
    sequence_number = int
    tick_closures = List[TickClosure]
    synchronizer_actions = List[SynchronizerAction]

    def __init__(
            self,
            has_synchronizer_action: bool,
            all_tick_closures_are_empty: bool,
            has_single_tick_closure: bool,
            has_tick_closures: bool,
            has_heartbeat_requests: bool,
            sequence_number: int,
            tick_closures: List[TickClosure],
            synchronizer_actions: List[SynchronizerAction]
    ) -> None:
        self.has_synchronizer_action = has_synchronizer_action
        self.all_tick_closures_are_empty = all_tick_closures_are_empty
        self.has_single_tick_closure = has_single_tick_closure
        self.has_tick_closures = has_tick_closures
        self.has_heartbeat_requests = has_heartbeat_requests
        self.sequence_number = sequence_number
        self.tick_closures = tick_closures
        self.synchronizer_actions = synchronizer_actions

    @classmethod
    def from_bitstream(cls, bit_stream: BitStream):
        _, has_synchronizer_action, all_tick_closures_are_empty, has_single_tick_closure, has_tick_closures, has_heartbeat_requests = bit_stream.readlist(
            "b3, bool, bool, bool, bool, bool")
        sequence_number = bit_stream.read("uintle32")

        tick_closures = []

        if has_tick_closures:
            if has_single_tick_closure:
                tick_closures.append(TickClosure.from_bitstream(
                    bit_stream, all_tick_closures_are_empty))
                if not bit_stream.pos == len(bit_stream):
                    raise NotImplementedError(
                        "possible segmented input action can not be decoded")
            else:
                raise NotImplementedError(
                    "decoding of multiple tick closures not implemented.")
            
        synchronizer_actions = []

        if has_synchronizer_action:
            amount_of_synchronizer_actions = bit_stream.read("uintle8")
            for _ in range(amount_of_synchronizer_actions):
                synchronizer_actions.append(SynchronizerAction.from_bitstream(bit_stream, True))

        if has_heartbeat_requests:
            raise NotImplementedError(
                "decoding of heartbeat requests is not implemented.")

        return cls(has_synchronizer_action, all_tick_closures_are_empty, has_single_tick_closure, has_tick_closures, has_heartbeat_requests, sequence_number, tick_closures, synchronizer_actions)

    def to_bitstream(self) -> BitStream:
        return_stream = BitStream(f"b3=0b000, bool={self.has_synchronizer_action}, bool={self.all_tick_closures_are_empty}, bool={
                                  self.has_single_tick_closure}, bool={self.has_tick_closures}, bool={self.has_heartbeat_requests}")
        return_stream += BitStream(f"uintle32={self.sequence_number}")
        if self.has_tick_closures:
            if not self.has_single_tick_closure:
                raise NotImplementedError(
                    "encoding of multiple tick closures not implemented")
            for tick_closure in self.tick_closures:
                return_stream += tick_closure.to_bitstream()

        if self.has_synchronizer_action:
            return_stream += BitStream(f"uintle8={len(self.synchronizer_actions)}")
            for synchronizer_action in self.synchronizer_actions:
                return_stream += synchronizer_action.to_bitstream()
        
        return return_stream
    
    def __str__(self) -> str:
        return super().__str__()


class ClientToServerHeartbeatPayload(MessagePayload):
    has_synchronizer_action: bool
    all_tick_closures_are_empty: bool
    has_single_tick_closure: bool
    has_tick_closures: bool
    has_heartbeat_requests: bool
    sequence_number = int
    tick_closures = List[TickClosure]
    next_to_receive_server_tick_closure = int
    synchronizer_actions = List[SynchronizerAction]

    def __init__(
            self,
            has_synchronizer_action: bool,
            all_tick_closures_are_empty: bool,
            has_single_tick_closure: bool,
            has_tick_closures: bool,
            has_heartbeat_requests: bool,
            sequence_number: int,
            tick_closures: List[TickClosure],
            next_to_receive_server_tick_closure: int,
            synchronizer_actions: List[SynchronizerAction]
    ) -> None:
        self.has_synchronizer_action = has_synchronizer_action
        self.all_tick_closures_are_empty = all_tick_closures_are_empty
        self.has_single_tick_closure = has_single_tick_closure
        self.has_tick_closures = has_tick_closures
        self.has_heartbeat_requests = has_heartbeat_requests
        self.sequence_number = sequence_number
        self.tick_closures = tick_closures
        self.next_to_receive_server_tick_closure = next_to_receive_server_tick_closure
        self.synchronizer_actions = synchronizer_actions

    @classmethod
    def from_bitstream(cls, bit_stream: BitStream):
        _, has_synchronizer_action, all_tick_closures_are_empty, has_single_tick_closure, has_tick_closures, has_heartbeat_requests = bit_stream.readlist(
            "b3, bool, bool, bool, bool, bool")
        sequence_number = bit_stream.read("uintle32")

        tick_closures = []

        if has_tick_closures:
            if has_single_tick_closure:
                tick_closures.append(TickClosure.from_bitstream(
                    bit_stream, all_tick_closures_are_empty))
            else:
                amount_of_tick_closures = bit_stream.read("uintle8")
                for _ in range(amount_of_tick_closures):
                    tick_closures.append(TickClosure.from_bitstream(
                        bit_stream, all_tick_closures_are_empty))

        if has_heartbeat_requests:
            raise NotImplementedError(
                "decoding of heartbeat requests is not implemented.")

        next_to_receive_server_tick_closure = bit_stream.read("uintle32")


        synchronizer_actions = []

        if has_synchronizer_action:
            amount_of_synchronizer_actions = bit_stream.read("uintle8")
            for _ in range(amount_of_synchronizer_actions):
                synchronizer_actions.append(SynchronizerAction.from_bitstream(bit_stream, False))

        return cls(has_synchronizer_action, all_tick_closures_are_empty, has_single_tick_closure, has_tick_closures, has_heartbeat_requests, sequence_number, tick_closures, next_to_receive_server_tick_closure, synchronizer_actions)

    def to_bitstream(self) -> BitStream:
        return_stream = BitStream(f"b3=0b000, bool={self.has_synchronizer_action}, bool={self.all_tick_closures_are_empty}, bool={
                                  self.has_single_tick_closure}, bool={self.has_tick_closures}, bool={self.has_heartbeat_requests}")
        return_stream += BitStream(f"uintle32={self.sequence_number}")
        if self.has_tick_closures:
            if not self.has_single_tick_closure:
                return_stream += BitStream(
                    f"uintle8={len(self.tick_closures)}")
            for tick_closure in self.tick_closures:
                return_stream += tick_closure.to_bitstream()
        
        return_stream += BitStream(
            f"uintle32={self.next_to_receive_server_tick_closure}")

        if self.has_synchronizer_action:
            return_stream += BitStream(f"uintle8={len(self.synchronizer_actions)}")
            for synchronizer_action in self.synchronizer_actions:
                return_stream += synchronizer_action.to_bitstream()

        return return_stream
    
    def __str__(self) -> str:
        return super().__str__()
