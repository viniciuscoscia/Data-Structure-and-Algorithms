def fast_select(array, index):  # k is an index
    array_length = len(array)  # length of the original array

    if 0 < index <= array_length:  # k should be a valid index
        # Helper variables
        set_of_medians = []
        arr_less_p = []
        arr_equal_p = []
        arr_more_p = []
        i = 0

        # Step 1 - Break Arr into groups of size 5
        # Step 2 - For each group, sort and find median (middle). Add the median to set_of_medians
        while i < array_length // 5:  # array_length//5 gives the integer quotient of the division
            median = find_median(array, start=5 * i, size=5)  # find median of each group of size 5
            set_of_medians.append(median)
            i += 1

        # If array_length is not a multiple of 5, then a last group with size = array_length % 5 will be formed
        if 5 * i < array_length:
            median = find_median(array, start=5 * i, size=array_length % 5)
            set_of_medians.append(median)

        # Step 3 - Find the median of set_of_medians
        if len(set_of_medians) == 1:  # Base case for this task
            pivot = set_of_medians[0]
        else:  # Bigger than one
            pivot = fast_select(array=set_of_medians, index=(len(set_of_medians) // 2))

        # Step 4 - Partition the original Arr into three sub-arrays
        for element in array:
            if element < pivot:
                arr_less_p.append(element)
            elif element > pivot:
                arr_more_p.append(element)
            else:
                arr_equal_p.append(element)

        # Step 5 - Recurse based on the sizes of the three sub-arrays
        if index <= len(arr_less_p):
            return fast_select(array=arr_less_p, index=index)

        elif index > (len(arr_less_p) + len(arr_equal_p)):
            return fast_select(array=arr_more_p, index=(index - len(arr_less_p) - len(arr_equal_p)))

        else:
            return pivot

        # Helper function


def find_median(array, start, size):
    my_list = []
    for i in range(start, start + size):
        my_list.append(array[i])

        # Sort the array
    my_list.sort()

    # Return the middle element
    return my_list[size // 2]


Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42]
k = 2
print(fast_select(Arr, k))  # Outputs 12

Arr = [5, 2, 20, 17, 11, 13, 8, 9, 11]
k = 5
print(fast_select(Arr, k))  # Outputs 11

Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]
k = 10
print(fast_select(Arr, k))  # Outputs 99
