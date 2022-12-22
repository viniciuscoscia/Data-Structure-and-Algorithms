class Stack:
    def __init__(self, initial_size=10):
        self.arr = [None for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0

    def push(self, value):
        if self.next_index == len(self.arr):
            self.on_full_stack()

        self.arr[self.next_index] = value
        self.next_index += 1
        self.num_elements += 1

    def __iter__(self):
        for value in range(self.num_elements):
            yield value

    def __repr__(self):
        return str([v for v in self])

    def on_full_stack(self):
        old_array = self.arr
        self.arr = [None for _ in range(2 * len(old_array))]
        for index, element in enumerate(old_array):
            self.arr[index] = element

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def pop(self):
        if self.is_empty():
            self.next_index = 0
            return None
        self.next_index -= 1
        self.num_elements -= 1
        return self.arr[self.next_index]

