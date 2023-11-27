def calculate_operations(arg_a, arg_b):
    results = (
        f"a + b = {arg_a + arg_b}",
        f"a - b = {arg_a - arg_b}",
        f"a * b = {arg_a * arg_b}",
        f"a / b = {arg_a / arg_b}",
        f"a ** b = {arg_a ** arg_b}",
        f"a // b = {arg_a // arg_b}",
        f"a % b = {arg_a % arg_b}"
    )
    return results


try:
    a = float(input("Enter value for a: "))
    b = float(input("Enter value for b: "))
    formatted_rows = calculate_operations(a, b)
    for row in formatted_rows:
        print(row)
except ZeroDivisionError:
    print("Cannot perform floor division by zero.")
except OverflowError:
    print("Result too large. Please use lower values")
except ValueError:
    print("Invalid input. Please enter numeric values.")
