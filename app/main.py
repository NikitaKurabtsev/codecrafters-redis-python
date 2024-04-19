import socket
import asyncio
from asyncio import StreamReader, StreamWriter

from .constants import (
    SERVER_HOST,
    SERVER_PORT,
    MAX_BUFFER_SIZE,
)

PONG = b"+PONG\r\n"

# TODO: Implement redis SimpleString Encoder

def simple_string_encoder(string: bytes) -> bytes:
    encoded_string = f"+ {string} \r\n".encode()
    return encoded_string


async def handle_client_connection(reader: StreamReader, writer: StreamWriter) -> None:
    while True:
        input_stream = await reader.read(MAX_BUFFER_SIZE)
        parsed_stream_data = input_stream.split(b"\r\n")[-2]
        message = simple_string_encoder(parsed_stream_data)
        if not input_stream:
            break
        if parsed_stream_data == b"ping":
            writer.write(PONG)
        else:
            writer.write(message)
        await writer.drain()
    writer.close()
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(handle_client_connection, SERVER_HOST, SERVER_PORT)
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
