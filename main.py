import atexit
import json
from logging import Logger
from pydoc import cli
from re import M
import socket
import logging.config
from typing import Any, Dict, Tuple


SOURCE_PORT = 1234
DESTINATION_PORT = 34197

SOURCE_IP = "127.0.0.1"
DESTINATION_IP = "127.0.0.1"

LOGGER = logging.getLogger("FactorioProxy")

def setup_logging() -> None:
    with open("logger_config.json") as f:
        config = json.load(f)
    logging.config.dictConfig(config)
    queue_handler = logging.getHandlerByName("queue_handler")
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)


def byte_to_binary_string(byte: int) -> str:
    return format(byte, '08b')

def left_pop_bytes(bytes_: bytes, amount: int) -> Tuple[bytes, bytes]:
    return bytes_[:amount], bytes_[amount:]

def handle_connection_request(message: bytes) -> None:
    connection_request = dict()
    connection_request["major_version"] = message[3]
    connection_request["minor_version"] = message[4]
    connection_request["patch"] = message[5]
    connection_request["build"] = int.from_bytes(message[6:8], "little")
    connection_request["connection_id"] = int.from_bytes(message[-4:], "little")
    LOGGER.info(f"ConnecitonRequest: {connection_request}")

def handle_transfer_block(message: bytes) -> None:
    transfer_block = dict()
    transfer_block["block_number"] = int.from_bytes(message[1:5], "little")
    LOGGER.debug(f"TransferBlock: {transfer_block}")

def handle_transfer_block_request(message: bytes) -> None:
    transfer_block_request = dict()
    transfer_block_request["block_number"] = int.from_bytes(message[1:5], "little")
    LOGGER.debug(f"TransferBlockRequest: {transfer_block_request}")

def handle_client_to_server_heartbeat(message: bytes) -> None:
    _, message = left_pop_bytes(message, 1)
    client_to_server_heartbeat = dict()
    flag_byte, message = left_pop_bytes(message, 1)
    client_to_server_heartbeat["flags"] = extract_heartbeat_flags(int.from_bytes(flag_byte))
    sequence_number_bytes, message = left_pop_bytes(message, 4)
    client_to_server_heartbeat["sequence_number"] = int.from_bytes(sequence_number_bytes, "little")
    if client_to_server_heartbeat["flags"]["has_tick_closures"]:
        client_to_server_heartbeat["tick_closures"] = []
        if client_to_server_heartbeat["flags"]["has_single_tick_closure"]:
            update_tick_bytes, message = left_pop_bytes(message, 4)
            client_to_server_heartbeat["tick_closures"].append({"update-tick": int.from_bytes(update_tick_bytes, "little")})
            if not client_to_server_heartbeat["flags"]["all_tick_closures_are_empty"]:
                nr_of_input_actions_byte, message = left_pop_bytes(message, 1)
                client_to_server_heartbeat["tick_closures"][-1]["input-actions"] = []
                for _ in range(int.from_bytes(nr_of_input_actions_byte)):
                    input_action, message = handle_input_action(message)
                    LOGGER.info(f"input_action: {input_action}")
                    client_to_server_heartbeat["tick_closures"][-1]["input-actions"].append(input_action)
        else:
            update_ticks_size_byte, message = left_pop_bytes(message, 1)
            client_to_server_heartbeat_tick_closures_size = int.from_bytes(update_ticks_size_byte)
            for _ in range(client_to_server_heartbeat_tick_closures_size):
                update_tick_bytes, message = left_pop_bytes(message, 4)
                client_to_server_heartbeat["tick_closures"].append({"update-tick": int.from_bytes(update_tick_bytes, "little")})
    next_to_receive_server_tick_closure_bytes, message = left_pop_bytes(message, 4)
    client_to_server_heartbeat["next_to_receive_server_tick_closure"] = int.from_bytes(next_to_receive_server_tick_closure_bytes, "little")
    if client_to_server_heartbeat["flags"]["has_synchronizer_action"]:
        client_to_server_heartbeat["synchronizer_actions"] = dict()
        synchronizer_actions_size_bytes, message = left_pop_bytes(message, 1)
        client_to_server_heartbeat["synchronizer_actions"]["size"] = int.from_bytes(synchronizer_actions_size_bytes)
        client_to_server_heartbeat["synchronizer_actions"]["actions"] = []
        for _ in range(client_to_server_heartbeat["synchronizer_actions"]["size"]):
            action, message = handle_synchronizer_action(message)
            client_to_server_heartbeat["synchronizer_actions"]["actions"].append(action)
    LOGGER.debug(f"ClientToServerHeartbeat: {client_to_server_heartbeat}")

def handle_input_action(message: bytes) -> Tuple[Dict[Any, Any], bytes]:
    input_action_type, input_action_payload_length = get_input_action_type_and_length(message)
    input_action_payload, message = left_pop_bytes(message, input_action_payload_length)

    return {"action_type": input_action_type, "action_payload": input_action_payload}, message

def get_input_action_type_and_length(message: bytes) -> Tuple[str, int]:
    match message[0]:
        case 0x3d:
            return "StartWalking", 3
        case 0x01:
            return "StopWalking", 2
        case 0xca:
            return "SelectedEntityChangedBasedOnUnitNumber", 6
        case 0xc8:
            return "SelectedEntityChangedVeryClosePrecise", 4
        case 0x00:
            return "Nothing", 2
        case 0x0b:
            return "SelectedEntityCleared", 2
        case 0x02:
            return "BeginMining", 2
        case 0x03:
            return "StopMining", 2
        
        case _:
            LOGGER.warning(f"Unknown input action type: {message[0]}")
            return "", 1

def extract_heartbeat_flags(byte: int) -> Dict[str, bool]:
    flag_bits = byte_to_binary_string(byte)
    flags = dict()
    flags["has_heartbeat_requests"] = bool(int(flag_bits[-1]))
    flags["has_tick_closures"] = bool(int(flag_bits[-2]))
    flags["has_single_tick_closure"] = bool(int(flag_bits[-3]))
    flags["all_tick_closures_are_empty"] = bool(int(flag_bits[-4]))
    flags["has_synchronizer_action"] = bool(int(flag_bits[-5]))
    return flags

def handle_synchronizer_action(message: bytes) -> Tuple[Dict[Any, Any], bytes]:
    action_type, action_payload_length = get_synchronizer_action_type_and_length(message)
    action_payload, message = left_pop_bytes(message, action_payload_length)
    action_payload = action_payload[1:]

    return {"action_type": action_type, "action_payload": action_payload}, message

def get_synchronizer_action_type_and_length(action: bytes) -> Tuple[str, int]:
    match action[0]:
        case 0x01:
            return "PeerDisconnect", 2
        case 0x03:
            return "ClientChangedState", 2
        case _:
            LOGGER.warning(f"Unknown synchronizer action type: {action[0]}")
            return "", 1


def get_message_type(message: bytes) -> str:
    first_byte = byte_to_binary_string(message[0])
    match first_byte[3:]:
        case "00010":
            return "ConnectionRequest"
        case "00011":
            return "ConnectionRequestReply"
        case "00100":
            return "ConnectionRequestReplyConfirm"
        case "00101":
            return "ConnectionAcceptOrDeny"
        case "00111":
            return "ServerToClientHeartbeat"
        case "00110":
            return "ClientToServerHeartbeat"
        case "01100":
            return "TransferBlockRequest"
        case "01101":
            return "TransferBlock"
        case _:
            return "Undefined"

def handle_message(message: bytes) -> None:
    message_type = get_message_type(message)
    match message_type:
        case "ConnectionRequest":
            handle_connection_request(message)
        case "TransferBlockRequest":
            handle_transfer_block_request(message)
        case "TransferBlock":
            handle_transfer_block(message)
        case "ClientToServerHeartbeat":
            handle_client_to_server_heartbeat(message)
        case "Undefined":
            LOGGER.debug(message)
        case _:
            LOGGER.debug(message_type)


if __name__ == "__main__":
    setup_logging()
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as proxy_socket:
        proxy_socket.bind((SOURCE_IP, SOURCE_PORT))

        server_address = (DESTINATION_IP, DESTINATION_PORT)
        client_address = None

        while True:
            data, address = proxy_socket.recvfrom(1024)
            handle_message(data)
            if address != server_address:
                client_address = address
                proxy_socket.sendto(data, server_address)
            elif address == server_address and client_address is not None:
                proxy_socket.sendto(data, client_address)
