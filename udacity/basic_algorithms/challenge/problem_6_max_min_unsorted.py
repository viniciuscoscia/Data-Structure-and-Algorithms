import random


def get_min_max(ints):
    """
    Return a tuple(min_value, max_value) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None, None

    max_value = float('-inf')
    min_value = float('inf')

    for value in ints:
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value

    return min_value, max_value


## Example Test Case of Ten Integers
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Big range
l = [i for i in range(0, 1000000)]  # a list containing 0 - 9
random.shuffle(l)
print("Pass" if ((0, 999999) == get_min_max(l)) else "Fail")

# Empty
l = []  # a list containing 0 - 9
random.shuffle(l)
print("Pass" if ((None, None) == get_min_max(l)) else "Fail")

# Single Value
l = [12345]  # a list containing 0 - 9
print("Pass" if ((12345, 12345) == get_min_max(l)) else "Fail")
