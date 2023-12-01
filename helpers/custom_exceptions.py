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
