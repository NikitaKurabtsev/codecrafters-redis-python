import socket
from threading import Thread

from .constants import (
    SERVER_HOST,
    SERVER_PORT,
    MAX_BUFFER_SIZE,
)


def connection_handeler(client_connection: socket.socket) -> None:
    # data = client_connection.recv(MAX_BUFFER_SIZE)

    response = b"+PONG\r\n"

    client_connection.sendall(response)


def main():
    server_socket = socket.create_server((SERVER_HOST, SERVER_PORT), reuse_port=True)
    while True:
        client_socket = server_socket.accept()[0]
        thread = Thread(target=connection_handeler, args=[client_socket])
        thread.start()


if __name__ == "__main__":
    main()
