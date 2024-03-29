def heapify(arr, array_size, current_node_index):
    print(f'array_size = {array_size}, current_node_index={current_node_index}, {arr}')
    # Using i as the index of the current node, find the 2 child nodes (if the array were a binary tree)
    # and find the largest value.   If one of the children is larger swap the values and recurse into that subree

    # consider current index as largest
    largest_index = current_node_index
    left_node_index = 2 * current_node_index + 1
    right_node_index = 2 * current_node_index + 2

    # compare with left child
    if left_node_index < array_size and arr[current_node_index] < arr[left_node_index]:
        left_value = arr[left_node_index]
        print(f'left_node_index ({left_value})  < array_size')
        largest_index = left_node_index

    # compare with right child
    if right_node_index < array_size and arr[largest_index] < arr[right_node_index]:
        right_value = arr[right_node_index]
        print(f'right_node_value ({right_value}) < array_size')
        largest_index = right_node_index

    # if either of left / right child is the largest node
    if largest_index != current_node_index:
        print(f'{arr[current_node_index]} troca com {arr[largest_index]}')
        arr[current_node_index], arr[largest_index] = arr[largest_index], arr[current_node_index]
        heapify(arr, array_size, largest_index)


def heapsort(arr):
    # First convert the array into a maxheap by calling heapify on each node, starting from the end
    # now that you have a maxheap, you can swap the first element (largest) to the end (final position)
    # and make the array minus the last element into maxheap again.  Continue to do this until the whole
    # array is sorted
    n = len(arr)

    print('BUILD A MAXHEAP.')
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)

    print('EXTRACT ELEMENTS.')
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


def test_function(test_case):
    heapsort(test_case[0])
    if test_case[0] == test_case[1]:
        print("Pass")
    else:
        print("False")


arr = [7, 3, 5, 1, 2, 4, 9, 6]
solution = [1, 2, 3, 4, 5, 6, 7, 9]
test_case = [arr, solution]
test_function(test_case)

arr = [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]
solution = [0, 1, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9]
test_case = [arr, solution]
test_function(test_case)

arr = [5, 5, 5, 3, 3, 3, 4, 4, 4, 4]
solution = [3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
test_case = [arr, solution]
test_function(test_case)

arr = [99]
solution = [99]
test_case = [arr, solution]
test_function(test_case)

arr = [0, 1, 2, 5, 12, 21, 0]
solution = [0, 0, 1, 2, 5, 12, 21]
test_case = [arr, solution]
test_function(test_case)
