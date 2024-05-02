from typing import Tuple

class InputStreamParser:
    @staticmethod
    def parse_command(input_stream: bytes) -> bytes:
        """Parses the command from the input stream."""
        command = input_stream.split(b"\r\n")[2]

        return command

    @staticmethod
    def parse_key_value_expiry(input_stream: bytes) -> Tuple[bytes, bytes, bytes]:
        """Parses the key and value from the input stream."""
        request_data = input_stream.split(b"\r\n")
        key = request_data[4]
        value = request_data[6]
        expiry = request_data[-2]

        return key, value, expiry
