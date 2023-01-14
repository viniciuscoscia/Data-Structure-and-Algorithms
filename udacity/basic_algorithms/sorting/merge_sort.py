def mergesort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


test_list_1 = [8, 3, 1, 7, 0, 10, 2]
test_list_2 = [1, 0]
test_list_3 = [97, 98, 99]
print('{} to {}'.format(test_list_1, mergesort(test_list_1)))
print('{} to {}'.format(test_list_2, mergesort(test_list_2)))
print('{} to {}'.format(test_list_3, mergesort(test_list_3)))


def merge_and_count(arr, left_start_index, left_end_index, right_start_index, right_end_index):
    sorted_array_size = (left_end_index - left_start_index + 1) + (right_end_index - right_start_index + 1)
    sorted_array = [None for _ in range(sorted_array_size)]
    sorted_array_index = 0
    left_index = left_start_index
    right_index = right_start_index
    inversions = 0

    while left_index <= left_end_index:
        left_value = arr[left_index]
        right_value = arr[right_index]

        if left_value <= right_value:  # All good, add it to the output
            left_index += 1
            sorted_array[sorted_array_index] = left_value
        else:
            inversions += (left_end_index - left_index + 1)
            right_index += 1
            sorted_array[sorted_array_index] = right_value

        sorted_array_index += 1

        if right_index > right_end_index:
            while left_index <= left_end_index:
                sorted_array[sorted_array_index] = (arr[left_index])
                sorted_array_index += 1
                left_index += 1
            break
        elif left_index > left_end_index:
            while right_index <= right_end_index:
                sorted_array[sorted_array_index] = (arr[right_index])
                sorted_array_index += 1
                right_index += 1
            break

    if inversions > 0:
        sorted_array_index = 0
        for index in range(left_start_index, right_end_index + 1):
            arr[index] = sorted_array[sorted_array_index]
            sorted_array_index += 1

    return inversions


def _count_inversions(arr, start_index, end_index) -> int:
    if start_index >= end_index:
        return 0

    mid_index = start_index + (end_index - start_index) // 2

    left_start_index = start_index
    left_end_index = mid_index

    right_start_index = mid_index + 1
    right_end_index = end_index

    left = _count_inversions(arr, left_start_index, left_end_index)
    right = _count_inversions(arr, right_start_index, right_end_index)

    return left + right + merge_and_count(
        arr,
        left_start_index,
        left_end_index,
        right_start_index,
        right_end_index
    )


def count_inversions(arr):
    if len(arr) < 2:
        return 0

    start_index = 0
    end_index = len(arr) - 1

    inversions = _count_inversions(arr, start_index, end_index)

    return inversions


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    count = count_inversions(arr)
    print(f'count = {count} - solution = {solution} ')
    if count == solution:
        print("Pass")
    else:
        print("Fail")


print('Test 1')
arr = [2, 5, 1, 3, 4]
solution = 4
test_case = [arr, solution]
test_function(test_case)

print('Test 2')
arr = [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
solution = 26
test_case = [arr, solution]
test_function(test_case)

print('Test 3')
arr = [1, 2, 4, 2, 3, 11, 22, 99, 108, 389]
solution = 2
test_case = [arr, solution]
test_function(test_case)

print('Test 4')
arr = [6, 7, 4, 9, 5, 3, 8, 1]
solution = 18
test_case = [arr, solution]
test_function(test_case)
