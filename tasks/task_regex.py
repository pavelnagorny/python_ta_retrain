import re
from helpers.custom_exceptions import InvalidInputFormat


def sell_car(car_info):
    year_match = re.search(r'\b(?:20|19)\d{2}\b', car_info)
    phone_match = re.findall(r'\+?\b(?:380\d{9}|\d{10})\b', car_info)
    vin_match = re.search(r'\b[A-HJ-NPR-Z0-9]{17}\b', car_info)
    license_plate_match = re.search(r'\b[A-Za-z]{2}\d{4}[A-Za-z]{2}\b', car_info)

    if not all([year_match, phone_match, vin_match, license_plate_match]):
        raise InvalidInputFormat()

    year = year_match.group()
    phone = phone_match[0]
    vin = vin_match.group()
    license_plate = license_plate_match.group()

    return [year, phone, vin, license_plate]
