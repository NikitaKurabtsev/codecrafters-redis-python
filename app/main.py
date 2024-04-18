import socket
from threading import Thread

from .constants import (
    SERVER_HOST,
    SERVER_PORT,
    MAX_BUFFER_SIZE,
)

PONG = b"+PONG\r\n"


def connection_handler(client_connection: socket.socket) -> None:
    while True:
        input_data = client_connection.recv(MAX_BUFFER_SIZE)
        if b"ping" in input_data:
            client_connection.sendall(PONG)


def main():
    server_socket = socket.create_server((SERVER_HOST, SERVER_PORT), reuse_port=True)
    while True:
        client_socket = server_socket.accept()[0]
        thread = Thread(target=connection_handler, args=[client_socket])
        thread.start()


if __name__ == "__main__":
    main()
