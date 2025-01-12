from typing import List


def plusOne(digits: List[int]) -> List[int]:
    increment_next = False

    if digits[len(digits) - 1] == 9:
        digits[len(digits) - 1] = 0
        increment_next = True
    else:
        digits[len(digits) - 1] = digits[len(digits) - 1] + 1

    for index in range(len(digits) - 2, -1, -1):
        print(index)
        if digits[index] == 9 and increment_next:
            digits[index] = 0
        elif increment_next:
            digits[index] = digits[index] + 1
            increment_next = False

    if increment_next:
        digits[0] = 1
        digits.append(0)

    return digits

print(plusOne([8,9,9,9]))

# Version from Claude AI
def plus_one(digits: List[int]) -> List[int]:
    """
    Add one to a number represented as a list of digits.

    Args:
        digits: List of integers where each integer is a single digit (0-9)

    Returns:
        List of integers representing the number after adding one

    Examples:
        >>> plus_one([1,2,3])
        [1,2,4]
        >>> plus_one([9,9,9])
        [1,0,0,0]
    """
    # Start from the rightmost digit
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    # If we're here, it means all digits were 9
    return [1] + [0] * len(digits)

print(plus_one([8,9,9,9]))  # [9,0,0,0]
print(plus_one([9,9,9]))    # [1,0,0,0]
print(plus_one([1,2,3]))    # [1,2,4]