def to_minutes(hours) -> int:
    """
    Convert hours to minutes.

    :param hours: The number of hours to be converted.
    :return: The equivalent number of minutes.
    :rtype: int
    """
    return int(hours * 60)


def to_hours(minutes) -> float:
    """
    Convert minutes to hours and round to 4 digits after the decimal point.

    :param minutes: The number of minutes to be converted.
    :return: The equivalent number of minutes.
    :rtype: float
    """
    return round((minutes / 60.0), 4)


def is_whole_div(dividend, divisor) -> bool:
    """
    Check if the division of the dividend by the divisor results in a whole number.

    :param dividend: The dividend in the division.
    :param divisor: The divisor in the division.
    :return: True if the division results in a whole number, False otherwise.
    :rtype: bool
    """
    return dividend % divisor == 0
