class Heap:
    def __init__(self, initial_size):
        self.cbt = [None for _ in range(initial_size)]  # initialize arrays
        self.next_index = 0  # denotes next index where new element should go

    def insert(self, data):
        """
        Insert `data` into the heap
        """
        if self.next_index > len(self.cbt) - 1:
            print(f'Heap is full, could not add {data}')
            return

        self.cbt[self.next_index] = data
        self.up_heapify()

        self.next_index += 1

        current_cbt_length = len(self.cbt)
        if self.next_index + 1 > current_cbt_length:
            new_cbt = [None for _ in range(current_cbt_length * 2)]
            for index, item in enumerate(self.cbt):
                new_cbt[index] = item
            self.cbt = new_cbt

    def up_heapify(self):
        if len(self.cbt) <= 1:
            return

        child_index = self.next_index
        child_data = self.cbt[child_index]

        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            parent_data = self.cbt[parent_index]

            if child_data < parent_data:
                self.cbt[parent_index] = child_data
                self.cbt[child_index] = parent_data
                child_index = parent_index
            else:
                break

    def remove(self):
        if self.next_index == 0:
            return None

        first_item = self.cbt[0]

        if self.next_index == 1:
            self.cbt[0] = None
            self.next_index -= 1
            return first_item

        self.next_index -= 1
        last_item = self.cbt[self.next_index]
        self.cbt[0], self.cbt[self.next_index] = last_item, None
        self.down_heapify()

        return first_item

    def down_heapify(self):
        if self.next_index == 0:
            return

        current_index = 0
        while current_index < self.next_index - 1:
            item = self.cbt[current_index]

            left_child_index = 2 * current_index + 1
            left_child = self.cbt[left_child_index]

            right_child_index = 2 * current_index + 2
            right_child = self.cbt[right_child_index]
            # [1, 1, 2, 4, 2, 3, None, None, None, None]
            if left_child is None:
                return
            elif (right_child is None and item > left_child) or (right_child is not None and left_child <= right_child):
                self.cbt[left_child_index] = item
                self.cbt[current_index] = left_child
                current_index = left_child_index
            elif right_child is not None:
                self.cbt[right_child_index] = item
                self.cbt[current_index] = right_child
                current_index = right_child_index
            else:
                return

    def get_minimum(self):
        # Returns the minimum element present in the heap
        if self.size() == 0:
            return None
        return self.cbt[0]

    def is_empty(self):
        return self.next_index == 0

    def size(self):
        return self.next_index


heap_size = 5
heap = Heap(heap_size)

elements = [1, 2, 3, 4, 1, 2]
for element in elements:
    heap.insert(element)
    # [1, 1, 2, 4, 2, 3, None, None, None, None]
print('Inserted elements: {}'.format(elements))
print('Formatted elements: {}'.format(heap.cbt))

print('size of heap: {}'.format(heap.size()))

for _ in range(4):
    print('Call remove: {}'.format(heap.remove()))

print('Call get_minimum: {}'.format(heap.get_minimum()))

for _ in range(2):
    print('Call remove: {}'.format(heap.remove()))

print('size of heap: {}'.format(heap.size()))
print('Call remove: {}'.format(heap.remove()))
print('Call is_empty: {}'.format(heap.is_empty()))
