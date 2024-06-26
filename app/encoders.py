def simple_string_encoder(input_stream: bytes) -> bytes:
    """
    Encodes the input stream according
    to the Redis protocol simple string format.
    """
    encoded_string = b"+" + input_stream + b"\r\n"

    return encoded_string


def bulk_string_encoder(input_stream: bytes) -> bytes:
    string_count = str(len(input_stream))
    encoded_string = b"$" + string_count.encode() + b"\r\n" + input_stream + b"\r\n"

    return encoded_string
