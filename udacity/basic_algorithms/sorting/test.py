import random


def test(start_index, end_index):
    mid_index = start_index + (end_index - start_index) // 2
    mid_index2 = (start_index + end_index) // 2

    print(f'{start_index} + ({end_index} - {start_index}) // 2 = {mid_index}')
    print(f'({start_index} + {end_index}) // 2 = {mid_index2}')
    print(mid_index == mid_index2)


test(8, 10)

# for _ in range(100):
#     test(random.randint(0, 100), random.randint(0, 100))
