import socket

from app.constants import (
    SERVER_HOST,
    SERVER_PORT,
)


def main():
    server_socket = socket.create_server((SERVER_HOST, SERVER_PORT), reuse_port=True)
    server_socket.accept()


if __name__ == "__main__":
    main()
