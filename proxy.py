from socket import socket, AF_INET, SOCK_DGRAM

from message_handlers import MessageHandler

class Proxy():
    factorio_server_ip: str
    factorio_server_port: int
    proxy_listen_ip: str
    proxy_listen_port: int
    message_handler: MessageHandler

    def __init__(
        self,
        message_handler: MessageHandler,
        factorio_server_ip: str = "127.0.0.1",
        factorio_server_port: int = 34197,
        proxy_listen_ip: str = "localhost",
        proxy_listen_port: int = 1234
    ) -> None:
        self.message_handler = message_handler
        self.factorio_server_ip = factorio_server_ip
        self.factorio_server_port = factorio_server_port
        self.proxy_listen_ip = proxy_listen_ip
        self.proxy_listen_port = proxy_listen_port

    def listen(self):
        with socket(AF_INET, SOCK_DGRAM) as proxy_socket:
            proxy_socket.bind((self.proxy_listen_ip, self.proxy_listen_port))

            server_address = (self.factorio_server_ip, self.factorio_server_port)
            client_address = None

            while True:
                original_data, address = proxy_socket.recvfrom(1024)

                reconstructed_data = self.message_handler.handle_message(original_data)

                if address != server_address:
                    client_address = address
                    proxy_socket.sendto(reconstructed_data, server_address)

                elif address == server_address and client_address is not None:
                    proxy_socket.sendto(reconstructed_data, client_address)
