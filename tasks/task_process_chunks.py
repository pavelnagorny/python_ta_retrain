def transform_chunk(chunk):
    """
        Transform a chunk of digits based on the sum of cubes of its digits.

        Parameters:
        - chunk (str): A string representing a chunk of digits.

        Returns:
        str: Transformed chunk based on the sum of cubes of its digits.
             If the sum is even, the chunk is reversed; otherwise, the first digit is moved to the end.
    """
    if sum(int(digit) ** 3 for digit in chunk) % 2 == 0:
        return chunk[::-1]
    else:
        return chunk[1:] + chunk[0]


def process_chunks(input_string, n):
    if n <= 0 or n > len(input_string):
        return ""

    chunks = [input_string[i:i + n] for i in range(0, len(input_string), n) if len(input_string[i:i + n]) == n]
    return "".join(map(transform_chunk, chunks))
