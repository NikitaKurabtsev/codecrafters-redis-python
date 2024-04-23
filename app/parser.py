from typing import Tuple

class InputStreamParser:
    @staticmethod
    def parse_command(input_stream: bytes) -> bytes:
        """Parses the command from the input stream."""
        command = input_stream.split(b"\r\n")[2]

        return command

    @staticmethod
    def parse_key_value(input_stream: bytes) -> Tuple[bytes, bytes]:
        """Parses the key and value from the input stream."""
        key = input_stream.split(b"\r\n")[-3]
        value = input_stream.split(b"\r\n")[-2]

        return key, value
