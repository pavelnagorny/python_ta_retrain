import pytest
from helpers.custom_exceptions import InvalidInputFormat
from tasks.task_regex import sell_car


# Test cases for valid data
input_data = [('For information on our latest 2021 model, contact us at +380501234567. '
               'The vehicle with license plate number KY2023AA and VIN ABCDEFGH123456789'
               ' is available for a test drive.',
               ['2021', '+380501234567', 'ABCDEFGH123456789', 'KY2023AA'])]


@pytest.mark.parametrize("input_string, expected_result", input_data)
def test_regex(input_string, expected_result):
    assert sell_car(input_string) == expected_result


# Test cases for catching custom error
input_data_neg = [
    "Reach us at +380501234567 for details on our 1829 lineup. Don't miss the car with license plate number AO1129OA, "
    "complete with the VIN WAUZZZ8T2BA104614.",
    "Feel free to call +38501234567 for information on our latest cars. Our 2008 models are equipped with license "
    "plate number BK8888AI and VIN WAUZZZ8T39A034101.",
    "Contact us at 0671234567 for information on our 2022 models. Check out the car with license plate number "
    "AA1234OO, featuring VIN 1234567890INVALID.",
    "For any inquiries, please call +380501234567 Explore our 2021 collection, with license plate number BK88991AA, "
    "and VIN WAUZZZ8T5CA041557.",
]


@pytest.mark.parametrize("input_string", input_data_neg)
def test_regex(input_string):
    with pytest.raises(InvalidInputFormat):
        sell_car(input_string)
