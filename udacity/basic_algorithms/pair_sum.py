def match_sum(arr, left_start_index, left_end_index, right_start_index, right_end_index, target):
    left_current_index = left_start_index
    right_current_index = right_start_index

    while left_current_index <= left_end_index:
        if arr[left_current_index] + arr[right_current_index] == target:
            return [arr[left_current_index], arr[right_current_index]]

        right_current_index += 1
        if right_current_index > right_end_index:
            right_current_index = right_start_index
            left_current_index += 1

        if left_current_index > left_end_index:
            return [None, None]


def search_for_pair(arr, start_index, end_index, target):
    input_size = end_index - start_index + 1

    if input_size < 2:
        return [None, None]

    mid_index = start_index + (end_index - start_index) // 2

    left_output = search_for_pair(arr, start_index, mid_index, target)
    if left_output != [None, None]:
        return left_output

    right_output = search_for_pair(arr, mid_index + 1, end_index, target)
    if right_output != [None, None]:
        return right_output

    return match_sum(arr, start_index, mid_index, mid_index + 1, end_index, target)


def pair_sum(arr, target):
    """
    :param: arr - input array
    :param: target - target value
    TODO: complete this method to find two numbers such that their sum is equal to the target
    Return the two numbers in the form of a sorted list
    """

    return search_for_pair(arr, 0, len(arr) - 1, target)


def test_function(test_case):
    input_list = test_case[0]
    target = test_case[1]
    solution = test_case[2]
    output = pair_sum(input_list, target)
    if output == solution:
        print("Pass")
    else:
        print("False")


input_list = [2, 7, 11, 15]
target = 9
solution = [2, 7]
test_case = [input_list, target, solution]
test_function(test_case)

input_list = [0, 8, 5, 7, 9]
target = 9
solution = [0, 9]
test_case = [input_list, target, solution]
test_function(test_case)

input_list = [110, 9, 89]
target = 9
solution = [None, None]
test_case = [input_list, target, solution]
test_function(test_case)
