import atexit
import json
import socket
import logging.config
from typing import Any, Dict, List, Tuple
from bitstring import BitStream
from input_action_type import INPUT_ACTION_LOOKUP_TABLE, InputActionType

from message_type import MessageType

PROXY_INPUT_PORT = 1234
FACTORIO_SERVER_PORT = 34197

PROXY_IP = "127.0.0.1"
FACTORIO_SERVER_IP = "127.0.0.1"

LOGGER = logging.getLogger("FactorioProxy")

def setup_logging() -> None:
    with open("logger_config.json") as f:
        config = json.load(f)
    logging.config.dictConfig(config)
    queue_handler = logging.getHandlerByName("queue_handler")
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)

def handle_message(message: bytes) -> None:
    # convert message to bitstream
    bit_stream = BitStream(message)

    # get headers
    last_fragment, fragmented, random, message_type = bit_stream.readlist("bool, bool, bool, uint5")
    message_type = MessageType(message_type)


    # handle fragmented data
    if fragmented:
        # get confirm flag and message id by reading and swaping bytes
        confirm_message_id = bit_stream.read("bits16")
        confirm_message_id.byteswap()
        confirm, message_id = confirm_message_id.readlist("bool, uint15")

        if confirm:
            fragment_number, confirm_count, confirm_data = bit_stream.readlist("uint8, uint8, bits32")
            # print(fragment_number, confirm_count, confirm_data.hex)
    
        if not (message_type == MessageType.ConnectionRequestReply or message_type == MessageType.ConnectionAcceptOrDeny):
            raise NotImplementedError("Decoding fragmented messages is not implemented!")
    
    # handle payload
    payload = bit_stream[bit_stream.pos:]
    decoded_payload = None
    match message_type:
        case MessageType.TransferBlockRequest:
            decoded_payload = handle_transfer_block_request(payload)
        case MessageType.TransferBlock:
            decoded_payload = handle_transfer_block(payload)
        case MessageType.ServerToClientHeartbeat:
            decoded_payload = handle_server_to_client_heartbeat(payload)
        case MessageType.ClientToServerHeartbeat:
            decoded_payload = handle_client_to_server_heartbeat(payload)
        case _:
            raise NotImplementedError(f"Message type not implemented {message_type}!")
    if decoded_payload is not None:
        LOGGER.debug(f"{message_type}: {decoded_payload}")
    else:
        LOGGER.debug(message_type)
            
def handle_transfer_block_request(payload: BitStream) -> Dict[str, Any]:
    block_number = payload.read("uintle32")
    return {"block_number": block_number}

def handle_transfer_block(payload: BitStream) -> Dict[str, Any]:
    block_number = payload.read("uintle32")
    data = payload[payload.pos:].hex
    return {"block_number": block_number, "data": data}

def handle_server_to_client_heartbeat(payload: BitStream) -> Dict[str, Any]:
    # decode flags
    flags_byte = payload.read("bits8")
    flags = decode_heartbeat_flags(flags_byte)

    # decode sequence number
    sequence_number = payload.read("uintle32")

    # decode tick closures
    if flags["has_tick_closures"]:
        tick_closures = []
        if flags["has_single_tick_closure"]:
            if not flags["all_tick_closures_are_empty"]:
                tick_closure, rest_payload = decode_single_tick_closure(payload[payload.pos:])
                tick_closures.append(tick_closure)
                payload = rest_payload
            else:
                raise NotImplementedError("Decoding single empty tick closure in ServerToClientHeartbeat not implemented")
        else:
            raise NotImplementedError("Decoding multiple tick closures in ServerToClientHeartbeat not implemented")
        return {"flags": flags, "sequence_number": sequence_number, "tick_closures": tick_closures}
    return {"flags": flags, "sequence_number": sequence_number}

def handle_client_to_server_heartbeat(payload: BitStream) -> Dict[str, Any]:
    # decode flags
    flags_byte = payload.read("bits8")
    flags = decode_heartbeat_flags(flags_byte)

    # decode sequence number
    sequence_number = payload.read("uintle32")

    # decode tick closures
    if flags["has_tick_closures"]:
        tick_closures = []
        if flags["has_single_tick_closure"]:
            if not flags["all_tick_closures_are_empty"]:
                tick_closure, rest_payload = decode_single_tick_closure(payload[payload.pos:])
                tick_closures.append(tick_closure)
                payload = rest_payload
            else:
                tick_closure, rest_payload = decode_empty_tick_closure(payload[payload.pos:])
                tick_closures.append(tick_closure)
                payload = rest_payload
        else:
            if flags["all_tick_closures_are_empty"]:
                amount_of_tick_closures = payload.read("uintle8")
                for _ in range(amount_of_tick_closures):
                    tick_closure, rest_payload = decode_empty_tick_closure(payload[payload.pos:])
                    tick_closures.append(tick_closure)
                    payload = rest_payload
            else:
                raise NotImplementedError("Decoding multiple non empty tick closures in ClientToServerHeartbeat not implemented")
        
    # get nextToRecieveServerTickClosure
    next_to_receive_server_tick_closure = payload.read("uintle32")

    # TODO decode synchronizer actions

    return_dict = {"flags": flags, "sequence_number": sequence_number, "next_to_receive_server_tick_closure": next_to_receive_server_tick_closure}
    if flags["has_tick_closures"]:
        return_dict["tick_closures"] = tick_closures
    return return_dict

def decode_heartbeat_flags(flags_byte: BitStream) -> Dict[str, bool]:
    _, has_synchronizer_action, all_tick_closures_are_empty, has_single_tick_closure, has_tick_closures, has_heartbeat_requests = flags_byte.readlist("b3, bool, bool, bool, bool, bool")
    return {
        "has_synchronizer_action": has_synchronizer_action, 
        "all_tick_closures_are_empty": all_tick_closures_are_empty, 
        "has_single_tick_closure": has_single_tick_closure, 
        "has_tick_closures": has_tick_closures, 
        "has_heartbeat_requests": has_heartbeat_requests
    }

def decode_empty_tick_closure(payload: BitStream) -> Tuple[Dict[str, Any], BitStream]:
    update_tick = payload.read("uintle32")
    return {"update_tick": update_tick}, payload[payload.pos:]

def decode_single_tick_closure(payload: BitStream) -> Tuple[Dict[str, Any], BitStream]:
    update_tick = payload.read("uintle32")
    input_actions, rest_payload = decode_input_actions(payload[payload.pos:])

    return {"update_tick": update_tick, "input_actions": input_actions}, rest_payload

def decode_input_actions(payload: BitStream) -> Tuple[List[Dict[str, Any]], BitStream]:
    input_action_amount = payload.read("uint8") // 2

    rest_payload = payload[payload.pos:]
    input_actions = []
    for i in range(input_action_amount):
        single_input_action, rest_payload = decode_single_input_action(rest_payload)
        input_actions.append(single_input_action)
    return input_actions, rest_payload

def decode_single_input_action(rest_payload: BitStream) -> Tuple[Dict[str, Any], BitStream]:
    input_action_type = InputActionType(rest_payload.read("uintle8"))
    maybe_player_index = rest_payload.read("uintle8")
    lookup_table_entry = INPUT_ACTION_LOOKUP_TABLE[input_action_type]
    if lookup_table_entry["length"] is None:
        raise NotImplementedError(f"Can not decode input action {input_action_type}, because length is unknown! Payload: {rest_payload[rest_payload.pos:]}")
    elif lookup_table_entry["decoder"] is None:
        raise NotImplementedError(f"No decoder implemented for input action {input_action_type}! Payload: {rest_payload[rest_payload.pos:rest_payload.pos+(lookup_table_entry["length"])*8]}")
    else:
        input_action_data, rest_payload = lookup_table_entry["decoder"](rest_payload[rest_payload.pos:])
        return {"input_action_type": input_action_type, "maybe_player_index": maybe_player_index, "input_action_data": input_action_data}, rest_payload



if __name__ == "__main__":
    setup_logging()
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as proxy_socket:
        proxy_socket.bind((PROXY_IP, PROXY_INPUT_PORT))

        server_address = (FACTORIO_SERVER_IP, FACTORIO_SERVER_PORT)
        client_address = None

        while True:
            data, address = proxy_socket.recvfrom(1024)
            try:
                handle_message(data)
            except NotImplementedError as e:
                LOGGER.info(e)
            except Exception as e:
                LOGGER.error(f"Unexpected Error during decoding. {e}")
            if address != server_address:
                client_address = address
                proxy_socket.sendto(data, server_address)
            elif address == server_address and client_address is not None:
                proxy_socket.sendto(data, client_address)
