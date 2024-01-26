import socket
import logging
import binascii

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

udp_ip = "127.0.0.1"
udp_port_in = 5000
upd_port_out = 34197

factorio_address_str = f"{udp_ip}:{upd_port_out}"
proxy_address_str = f"{udp_ip}:{udp_port_in}"


def ip_to_tuple(ip):
    ip, port = ip.split(':')
    return ip, int(port)


if __name__ == '__main__':

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(ip_to_tuple(proxy_address_str))

    factorio_address = ip_to_tuple(factorio_address_str)
    client_address = None

    while True:
        data, address = sock.recvfrom(1024)
        # print(f"recieved from: {address}")
        # print(f"recieved message: {data}")
        hex_data = ''.join([hex(thing) for thing in data])
        # print(hex_data)
        logging.debug({"from": address, "message": data})
        logging.debug({"hex": hex_data})

        # print(f"server_address: {factorio_address}")
        # print(f"client_address: {client_address}")

        if address != factorio_address:
            client_address = address
            sock.sendto(data, factorio_address)
        elif address == factorio_address:
            sock.sendto(data, client_address)
