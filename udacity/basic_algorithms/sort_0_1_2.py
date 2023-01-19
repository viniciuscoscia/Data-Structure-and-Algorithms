def sort_0_1_2(arr: list):
    index = 0
    zero_index = 0
    two_index = len(arr) - 1

    while index <= two_index:
        current_value = arr[index]

        if current_value == 0:
            arr[index], arr[zero_index] = arr[zero_index], current_value
            index += 1
            zero_index += 1
        elif current_value == 2:
            arr[index], arr[two_index] = arr[two_index], current_value
            two_index -= 1
        else:
            index += 1


def test_function(test_case):
    sort_0_1_2(test_case)
    print(test_case)
    if test_case == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_case = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
test_function(test_case)

test_case = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
test_function(test_case)

test_case = [2, 2, 0, 0, 2, 1, 0, 2, 2, 1, 1, 1, 0, 1, 2, 0, 2, 0, 1]
test_function(test_case)
