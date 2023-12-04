from tasks.task_process_chunks import process_chunks
import pytest


input_data = [("123456987654", 6, "234561876549"),
              ("123456987653", 6, "234561356789"),
              ("66443875", 4, "44668753"),
              ("66443875", 8, "64438756"),
              ("664438769", 8, "67834466"),
              ("123456779", 8, "23456771"),
              ("", 8, "ERROR: input_string should be a string of integers."),
              ("123456779", 0, "ERROR: n should be a positive integer."),
              ("123456", -4, "ERROR: n should be a positive integer."),
              ("625741", "4", "ERROR: n should be an integer."),
              ("123456", 7, "ERROR: input_string length should be greater than or equal to 'n'."),
              (12345, 4, "ERROR: input_string should be a string of integers.")]

@pytest.mark.parametrize("input_string, n, expected_result", input_data)
def test_process_chunks(input_string, n, expected_result):
    assert process_chunks(input_string, n) == expected_result
