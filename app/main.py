import socket
from threading import Thread
from typing import List

from .constants import (
    SERVER_HOST,
    SERVER_PORT,
    MAX_BUFFER_SIZE,
)


def input_commands_handler(input_data: bytes) -> List[bytes]:
    data = input_data.split(b" ")[2].split(b"\n")

    return data


def connection_handler(client_connection: socket.socket) -> None:
    input_data = client_connection.recv(MAX_BUFFER_SIZE)
    data = input_commands_handler(input_data)

    response = b"+PONG\r\n"

    for command in data:
        client_connection.sendall(response)


def main():
    server_socket = socket.create_server((SERVER_HOST, SERVER_PORT), reuse_port=True)
    while True:
        client_socket = server_socket.accept()[0]
        thread = Thread(target=connection_handler, args=[client_socket])
        thread.start()


if __name__ == "__main__":
    main()
