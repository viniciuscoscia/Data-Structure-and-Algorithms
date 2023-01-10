def binary_search(array, target):
    '''
    Write a function that implements the binary search algorithm using iteration

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''

    if len(array) == 0:
        return -1

    lower_bound_index = 0
    upper_bound_index = len(array) - 1

    while lower_bound_index <= upper_bound_index:
        if lower_bound_index == upper_bound_index:
            return -1

        current_index = (lower_bound_index + upper_bound_index) // 2
        current_value = array[current_index]

        if current_value == target:
            return current_index
        elif target > current_value:
            lower_bound_index = current_index + 1
        else:
            upper_bound_index = current_index - 1


def test_function(test_case):
    answer = binary_search(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
index = 6
test_case = [array, target, index]
test_function(test_case)


def binary_search_recursive(array, target):
    '''
    This function will call `binary_search_recursive_soln` function.
    You don't need to change this function.

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
    '''
    return binary_search_recursive_soln(array, target, 0, len(array) - 1)


def binary_search_recursive_soln(array, target, start_index, end_index):
    '''Write a function that implements the binary search algorithm using recursion

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
      start_index: beginning of the index of the sub-arrays
      end_index: end of the index of the sub-arrays

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    if start_index == end_index:
        return -1

    index = (start_index + end_index) // 2
    value = array[index]

    if value == target:
        return index
    elif target > value:
        return binary_search_recursive_soln(array, target, index + 1, end_index)
    else:
        return binary_search_recursive_soln(array, target, start_index, index - 1)


def test_function(test_case):
    answer = binary_search_recursive(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 4
index = 4
test_case = [array, target, index]
test_function(test_case)
