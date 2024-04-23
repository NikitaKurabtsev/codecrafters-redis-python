from typing import Tuple

class InputStreamParser:
    @staticmethod
    def simple_string_encoder(input_stream: bytes) -> bytes:
        """
        Encodes the input stream according
        to the Redis protocol simple string format.
        """
        encoded_string = b"+" + input_stream + b"\r\n"

        return encoded_string

    @staticmethod
    def parse_input_stream(input_stream: bytes) -> bytes:
        """Parses the command from the input stream."""
        parsed_data = input_stream.split(b"\r\n")[1]

        return parsed_data

    @staticmethod
    def parse_key_value(input_stream: bytes) -> Tuple[bytes, bytes]:
        """Parses the key and value from the input stream."""
        key = input_stream.split(b"\r\n")[-2]
        value = input_stream.split(b"\r\n")[-1]

        return key, value
