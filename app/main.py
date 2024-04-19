import socket
import asyncio
from asyncio import StreamReader, StreamWriter

from .constants import (
    SERVER_HOST,
    SERVER_PORT,
    MAX_BUFFER_SIZE,
)

PONG = b"+PONG\r\n"


async def handle_client_connection(reader: StreamReader, writer: StreamWriter) -> None:
    while True:
        input_stream = await reader.read(MAX_BUFFER_SIZE)
        parsed_stream_data = input_stream.split(b"\r\n")[-2]
        if not input_stream:
            break
        if parsed_stream_data == b"ping":
            writer.write(PONG)
        else:
            writer.write(parsed_stream_data)
        await writer.drain()
    writer.close()
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(handle_client_connection, SERVER_HOST, SERVER_PORT)
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
