import atexit
import json
import socket
import struct
import logging.config

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


if __name__ == "__main__":
    setup_logging()
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as proxy_socket:
        proxy_socket.bind((SOURCE_IP, SOURCE_PORT))

        server_address = (DESTINATION_IP, DESTINATION_PORT)
        client_address = None

        while True:
            data, address = proxy_socket.recvfrom(1024)
            if address != server_address:
                client_address = address
                proxy_socket.sendto(data, server_address)
            elif address == server_address and client_address is not None:
                proxy_socket.sendto(data, client_address)
