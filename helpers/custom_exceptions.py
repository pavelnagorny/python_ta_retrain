class ShortInputException(Exception):
    """Custom exception for invalid value length."""
    def __init__(self, parameter_name, length, at_least):
        super().__init__(f"Invalid input for {parameter_name}. Length {length} is less than {at_least}.")


class StartsWithLowerCaseError(ValueError):
    """Custom exception for strings that start with a lowercase letter."""
    def __init__(self, parameter_name):
        super().__init__(f"Invalid input for {parameter_name}. String should start with an uppercase letter.")


class InvalidAgeException(Exception):
    """Custom exception for invalid age values."""
    def __init__(self, parameter_name, min_age, max_age):
        super().__init__(f"Invalid input for {parameter_name}. Age should be in the range [{min_age}-{max_age}].")


class AlphaNumericError(Exception):
    """Raised when the input string is not a string of integers."""
    def __init__(self, parameter):
        super().__init__(f"{parameter} should be a string of integers.")


class NonIntegerError(TypeError):
    """Raised when n is not an integer."""
    def __init__(self, parameter="Input"):
        super().__init__(f"{parameter} should be an integer.")


class DivisionByZero(ZeroDivisionError):
    """Raised when divisor is 0."""
    def __init__(self):
        super().__init__(f"Divisor should not be equal to 0.")


class StringLengthError(Exception):
    """Raised when the input string length is less than n."""
    def __init__(self, parameter):
        super().__init__(f"{parameter} length should be greater than or equal to 'n'.")


class NegativeError(Exception):
    """Raised when n is not an integer."""
    def __init__(self, parameter):
        super().__init__(f"{parameter} should be a positive integer.")


class InvalidInputFormat(Exception):
    """Invalid input format"""
    pass
