import pytest
from helpers.custom_exceptions import (NonIntegerError, AlphaNumericError, StringLengthError, NegativeError)
from tasks.task_process_chunks import process_chunks


# Test cases for processing chunks with valid data
input_data = [
    ("123456987654", 6, "234561876549"),
    ("123456987653", 6, "234561356789"),
    ("66443875", 4, "44668753"),
    ("66443875", 8, "64438756"),
    ("664438769", 8, "67834466"),
    ("123456779", 8, "23456771")
]


@pytest.mark.parametrize("input_string, n, expected_result", input_data)
def test_process_chunks(input_string, n, expected_result):
    assert process_chunks(input_string, n) == expected_result


# Test cases for catching custom errors
input_data_neg = [
    ("", 8, AlphaNumericError),
    ("123456779", 0, NegativeError),
    ("123456", -4, NegativeError),
    ("625741", "4", NonIntegerError),
    ("123456", 7, StringLengthError),
    (12345, 4, AlphaNumericError)
]


@pytest.mark.parametrize("input_string, n, error", input_data_neg)
def test_process_chunks(input_string, n, error):
    with pytest.raises(error):
        process_chunks(input_string, n)
