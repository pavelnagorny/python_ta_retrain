from tasks.task_stat import stat
import pytest

test_array_1 = [3, 5, 1, 6, 4, 2, 5, 2, 3, 4, 2, 5, 5, 2]
test_array_2 = [2, 3, 2, 7, 8, 39, 2]
test_array_3 = [64, 41, 7, 41, 27, 38, 30, 45, 96, 0]


@pytest.mark.parametrize("test_data, expected_result", [(test_array_1, [14, 6, 2, [2, 5], [4, 4]]),
                                                        (test_array_2, [7, 5, 4, [2], [3]]),
                                                        (test_array_3, [10, 9, 8, [41], [2]])
                                                        ])
def test_stat(test_data, expected_result):
    assert stat(test_data) == expected_result
