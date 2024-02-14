from input_action import InputAction
from input_action.payloads import EmptyPayload
from input_action.types import InputActionType
from message_handlers import PassThroughHandler, LoggingHandler,ContinuousInputActionInjectionHandler, InputActionFilterHandler
from network_message.types import MessageType

from proxy import Proxy

import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Local Proxy to intercept and modify factorio network traffic.",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "mode",
        choices=["pass-through", "decode", "inject", "filter"],
        help=(
            "pass-through: Just passes the messages to the server without decoding or modifying them.\n"
            "decode: Tries to decode and log each message before re-encoding and sending it to the server.\n"
            "inject: Same as decode but also tries to inject a specified input action into each message.\n"
            "filter: !EXPERIMENTAL! Same as decode but also tries to filter all instances of the specified input action from each message."
        )
    )

    parser.add_argument(
        "--factorio_ip",
        action="store",
        default="127.0.0.1",
        help="IP address of the factorio server to forward to."
    )

    parser.add_argument(
        "--factorio_port",
        action="store",
        default=34197,
        help="Port of the factorio server to forward to."
    )

    parser.add_argument(
        "--listen_ip",
        action="store",
        default="localhost",
        help="IP address that the proxy should listen on."
    )

    parser.add_argument(
        "--listen_port",
        action="store",
        default=1234,
        help="Port that the proxy should listen on."
    )

    parser.add_argument(
        "--input_action_type",
        action="store",
        help="Only required in injection mode. Type of the input action to inject. Needs to be an exact match for a type defined in input_actions/types.py that accepts an empty payload."
    )

    parser.add_argument(
        "--message_type",
        action="store",
        help="Only required in injection mode. Must be ClientToServerHeartbeat or ServerToClientHeartbeat."
    )

    args = parser.parse_args()

    match args.mode:
        case "pass-through":
            message_handler = PassThroughHandler()
        case "decode":
            message_handler = LoggingHandler()
        case "inject":
            if args.input_action_type is None:
                parser.error(f"--input_action_type is required in injection mode. Needs to be an exact match for a type defined in input_actions/types.py that accepts an empty payload.")
            if args.message_type is None:
                parser.error("--message_type is required in injection mode. Must be ClientToServerHeartbeat or ServerToClientHeartbeat.")
            action_to_inject = InputAction(InputActionType[args.input_action_type], 0, EmptyPayload())
            message_handler = ContinuousInputActionInjectionHandler(action_to_inject, MessageType[args.message_type])
        case "filter":
            if args.input_action_type is None:
                parser.error(f"--input_action_type is required in filter mode. Needs to be an exact match for a type defined in input_actions/types.py that accepts an empty payload.")
            if args.message_type is None:
                parser.error("--message_type is required in filter mode. Must be ClientToServerHeartbeat or ServerToClientHeartbeat.")
            message_handler = InputActionFilterHandler(InputActionType[args.input_action_type], MessageType[args.message_type])

    proxy = Proxy(message_handler)
    proxy.listen()
