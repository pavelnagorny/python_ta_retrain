from helpers.custom_exceptions import (NonIntegerError, AlphaNumericError, StringLengthError, NegativeError)


def transform_chunk(chunk):
    if sum(int(digit) ** 3 for digit in chunk) % 2 == 0:
        return chunk[::-1]
    else:
        return chunk[1:] + chunk[0]


def process_chunks(input_string, n):
    if not isinstance(n, int):
        raise NonIntegerError(parameter="n")
    if isinstance(input_string, int) or not input_string.isdigit():
        raise AlphaNumericError(parameter="input_string")
    if len(input_string) < n:
        raise StringLengthError(parameter="input_string")
    if n <= 0:
        raise NegativeError(parameter="n")

    chunks = [input_string[i:i + n] for i in range(0, len(input_string), n) if len(input_string[i:i + n]) == n]
    return "".join(map(transform_chunk, chunks))
