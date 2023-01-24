def heapify(arr, array_size, current_node_index):
    largest_index = current_node_index
    left_node_index = 2 * current_node_index + 1
    right_node_index = 2 * current_node_index + 2

    if left_node_index < array_size and arr[current_node_index] < arr[left_node_index]:
        largest_index = left_node_index

    if right_node_index < array_size and arr[largest_index] < arr[right_node_index]:
        largest_index = right_node_index

    if largest_index != current_node_index:
        arr[current_node_index], arr[largest_index] = arr[largest_index], arr[current_node_index]
        heapify(arr, array_size, largest_index)


def rearrange_digits(input_list: list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    if input_list is None or len(input_list) < 1:
        return [0, 0]

    input_size = len(input_list)

    if input_size == 1:
        return [input_list[0], 0]

    for index in range((len(input_list) // 2) - 1, -1, -1):
        heapify(input_list, input_size, index)

    first_value = 0
    second_value = 0

    for index in range(input_size - 1, -1, -1):
        if index % 2 == 1:
            first_value = first_value * 10 + input_list[0]
        else:
            second_value = second_value * 10 + input_list[0]

        input_list[index], input_list[0] = input_list[0], input_list[index]  # swap
        heapify(input_list, index, 0)

    return [first_value, second_value]


def test_function(input, expected_output):
    output = rearrange_digits(input)
    if sum(output) == sum(expected_output):
        print("Pass")
    else:
        print("Fail")


# Normal cases
test_function(
    input=[4, 6, 2, 5, 9, 8],
    expected_output=[964, 852]
)

test_function(
    input=[1, 2, 3, 4, 5],
    expected_output=[542, 31]
)

# Repeated Numbers
test_function(
    input=[9, 9, 9, 9, 9, 9],
    expected_output=[999, 999]
)

test_function(
    input=[0, 0, 0, 0, 0],
    expected_output=[0, 0]
)

# Edge Cases
test_function(
    input=[],
    expected_output=[0, 0]
)

test_function(
    input=None,
    expected_output=[0, 0]
)

expected_output = 0
for _ in range(50):
    expected_output = expected_output * 10 + 9

test_function(
    input=[9] * 100,
    expected_output=[expected_output, expected_output]
)
