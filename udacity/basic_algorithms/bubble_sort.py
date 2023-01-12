def bubble_sort_1(values):
    last_index = len(values) - 1
    index = 0

    while last_index > 0:
        current_value = values[index]
        next_value = values[index + 1]

        if current_value > next_value:
            values[index], values[index + 1] = next_value, current_value

        if index + 1 == last_index:  # No need to check the last element, it should be sorted at this point
            print(values)
            index = 0
            last_index -= 1
        else:
            index += 1


wakeup_times = [16, 49, 3, 12, 56, 49, 55, 22, 13, 46, 19, 55, 46, 13, 25, 56, 9, 48, 45]

bubble_sort_1(wakeup_times)
print("Pass" if (wakeup_times[0] == 3) else "Fail")
