def simple_string_encoder(input_stream: bytes) -> bytes:
    """
    Encodes the input stream according
    to the Redis protocol simple string format.
    """
    encoded_string = b"+" + input_stream + b"\r\n"

    return encoded_string


def bulk_string_encoder(input_stream: bytes) -> str:
    string_count = str(len(str(input_stream)))
    encoded_string = "$" + string_count + "\r\n" + input_stream.decode() + "\r\n"

    return encoded_string
