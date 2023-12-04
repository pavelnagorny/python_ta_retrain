import pytest
from tasks.task_1_3 import to_minutes, to_hours, is_whole_div


# Test cases for to_minutes function
@pytest.mark.parametrize("hours, expected_minutes", [(0, 0), (1, 60),
                                                     (2.5, 150), (-1, -60)
                                                     ])
def test_to_minutes(hours, expected_minutes):
    result = to_minutes(hours)
    assert result == expected_minutes


# Test cases for to_hours function
@pytest.mark.parametrize("minutes, expected_hours", [(0, 0.0), (12, 0.2),
                                                     (5, 0.0833), (-120, -2.0)
                                                     ])
def test_to_hours(minutes, expected_hours):
    result = to_hours(minutes)
    assert result == expected_hours


# Test cases for is_whole_div function
@pytest.mark.parametrize("dividend, divisor, expected_result", [(10, 2, True), (10, 3, False),
                                                                (0, 5, True), (-15, 3, True),
                                                                ("6", 3, "ERROR: Input should be an integer."),
                                                                (4, "2", "ERROR: Input should be an integer."),
                                                                (8, 0, "ERROR: Divisor should not be equal to 0."),
                                                                (7, 3.5, "ERROR: Input should be an integer.")
                                                                ])
def test_is_whole_div(dividend, divisor, expected_result):
    result = is_whole_div(dividend, divisor)
    assert result == expected_result
