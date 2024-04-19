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
        print(input_stream)
        if not input_stream:
            break
        if input_stream == b"ping":
            writer.write(PONG)
        # else:
        #     input_stream_encoded = (b"+" + input_stream + b"\r\n")
        #     writer.write(input_stream_encoded)
        await writer.drain()
    writer.close()
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(handle_client_connection, SERVER_HOST, SERVER_PORT)
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
