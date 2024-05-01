import asyncio
import argparse
from asyncio import StreamReader, StreamWriter

from .constants import (
    SERVER_HOST,
    SERVER_PORT,
    MAX_BUFFER_SIZE,
    PONG,
    OK,
    NULL_BULK_STRING
)
from .database import RedisDataBaseManager
from .encoders import simple_string_encoder, bulk_string_encoder
from .parser import InputStreamParser

database_manager = RedisDataBaseManager()
parser = InputStreamParser()

async def handle_client_connection(reader: StreamReader, writer: StreamWriter) -> None:
    while True:
        input_stream = await reader.read(MAX_BUFFER_SIZE)
        print(input_stream.split(b"\r\n"))
        if not input_stream:
            break

        command = parser.parse_command(input_stream)
        message = simple_string_encoder(input_stream)

        if command == b"ping":
            encoded_message = simple_string_encoder(PONG)
            writer.write(encoded_message)

        elif command == b"echo":
            encoded_message = simple_string_encoder(input_stream.split(b"\r\n")[-2])
            writer.write(encoded_message)

        elif command == b"set":
            key, value = parser.parse_key_value(input_stream)
            database_manager.add_record(key, value)
            encoded_message = simple_string_encoder(OK.decode())
            writer.write(encoded_message)

        elif command == b"get":
            key = input_stream.split(b"\r\n")[-2]
            record = database_manager.fetch_record_by_key(key)

            if record:
                encoded_message = bulk_string_encoder(record.value)
            else:
                encoded_message = NULL_BULK_STRING
            writer.write(encoded_message)

        else:
            writer.write(message)

        await writer.drain()

    writer.close()
    await writer.wait_closed()


async def main(arguments):
    server = await asyncio.start_server(handle_client_connection, SERVER_HOST, arguments.port)
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("--port", default=6379)
    args = arg_parse.parse_args()
    asyncio.run(main(args))
