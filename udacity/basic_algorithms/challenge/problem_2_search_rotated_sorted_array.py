def calculate_mid_index(start_index, end_index):
    return start_index + (end_index - start_index) // 2


def find_pivot(array, start_index, end_index):
    if start_index == end_index:
        return end_index

    if end_index < start_index:
        return -1

    mid_index = calculate_mid_index(start_index, end_index)

    if array[mid_index] >= array[mid_index + 1]:
        return mid_index
    elif array[mid_index] < array[mid_index - 1]:
        return mid_index - 1
    elif array[mid_index] > array[end_index]:
        return find_pivot(array, mid_index + 1, end_index)
    else:
        return find_pivot(array, start_index, mid_index - 1)


def binary_search(array, start_index, end_index, number):
    if end_index < start_index:
        return -1

    mid_index = calculate_mid_index(start_index, end_index)

    if number == array[mid_index]:
        return mid_index
    elif number > array[mid_index]:
        return binary_search(array, mid_index + 1, end_index, number)
    else:
        return binary_search(array, start_index, mid_index - 1, number)


def rotated_array_search(input_list: list, number: int):
    """
    Find the index by searching in a rotated sorted array

    Args:
       :param input_list: Input array to search and the target
       :param number: Key to find on input list
    Returns:
       int: number index or -1 if not found
    """
    end_index = len(input_list) - 1
    pivot = find_pivot(input_list, 0, end_index)

    if pivot == -1:  # Sorted array
        return binary_search(input_list, 0, end_index, number)

    if input_list[pivot] == number:
        return pivot
    elif input_list[0] <= number:
        return binary_search(input_list, 0, pivot - 1, number)
    else:
        return binary_search(input_list, pivot + 1, end_index, number)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


# Sorted
test_function([[1, 2, 3, 4, 5, 6], 6])
test_function([[1, 2, 3, 4, 5, 6], 1])
test_function([[1, 2, 3, 4, 5, 6], 0])

# Unsorted
test_function([[3, 4, 6, 7, 8, 9, 10, 1, 2], 4])
test_function([[9, 10, 1, 2, 3, 4, 6, 7, 8], 4])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 4])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# Others
test_function([[], 1])
test_function([[], 0])
test_function([[1], 10])

# All should pass
