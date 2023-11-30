from collections import Counter


def stat(numbers: list) -> list:
    # (1) - Total amount of received integers.
    total_numbers_count = len(numbers)

    # (2) - Total amount of different values the array has.
    unique_numbers_count = len(set(numbers))

    # (3) - Total amount of values that occur only once.
    count_num_occurrence = Counter(numbers)  # Count occurrences of each element
    total_once_occurred_count = len([num for num, count in count_num_occurrence.items() if count == 1])

    # (4) - It is (or they are) the element(s) that has (or have) the maximum occurrence.
    # If there are more than one, the elements should be sorted (by their value obviously)
    max_occurrence = max(count_num_occurrence.values())  # Find the maximum occurrence
    most_occurred_numbers = [num for num, count in count_num_occurrence.items() if count == max_occurrence]
    sorted_most_occurred_numbers = sorted(most_occurred_numbers)

    # (5) - Maximum occurrence of the integer(s)
    max_count_of_integer = [count for num, count in count_num_occurrence.items() if count == max_occurrence]

    return [total_numbers_count, unique_numbers_count,
            total_once_occurred_count, sorted_most_occurred_numbers,
            max_count_of_integer]
