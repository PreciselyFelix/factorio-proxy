from input_action import InputAction
from input_action.payloads import EmptyPayload
from input_action.types import InputActionType
from message_handlers import PassThroughHandler, LoggingHandler,ContinuousInputActionInjectionHandler
from network_message.types import MessageType

from proxy import Proxy


if __name__ == "__main__":
    action_to_inject = InputAction(InputActionType.StopWalking, 0, EmptyPayload())
    message_handler = ContinuousInputActionInjectionHandler(action_to_inject, MessageType.ClientToServerHeartbeat)
    proxy = Proxy(message_handler)
    proxy.listen()
