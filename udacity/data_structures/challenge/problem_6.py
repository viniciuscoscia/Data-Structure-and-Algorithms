import random
import time
from datetime import timedelta
from timeit import default_timer as timer


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        new_tail = Node(value)

        if self.head is None:
            self.head = new_tail
            self.tail = new_tail
            return

        old_tail = self.tail
        old_tail.next = new_tail
        self.tail = new_tail

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def add_values_to_set(self, values_set: set):
        node = self.head
        while node:
            values_set.add(node.value)
            node = node.next
        return values_set


def union(llist_1, llist_2):
    values = set()

    llist_1.add_values_to_set(values)
    llist_2.add_values_to_set(values)

    return values


def intersection(linked_list_1, linked_list_2):
    list_1_values = set()

    linked_list_1.add_values_to_set(list_1_values)

    intersection_values = set()
    for element in linked_list_2:
        if element in list_1_values:
            intersection_values.add(element)

    return intersection_values


def remove_matching_values(set_from: set, set_to_compare: set):
    for element in set_to_compare:
        if element in set_from:
            set_from.remove(element)


def build_linked_lists(values1: list, values2: list):
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    for i in values1:
        linked_list_1.append(i)

    for i in values2:
        linked_list_2.append(i)

    return linked_list_1, linked_list_2


def test_operations_time(values1: list, values2: list):
    print("\n============== STARTING TEST ==============")
    linked_list_1, linked_list_2 = build_linked_lists(values1, values2)
    start = time.time()
    print(union(linked_list_1, linked_list_2))
    end = time.time()
    print(f'Union executed in {end - start} milliseconds')

    start = time.time()
    print(intersection(linked_list_1, linked_list_2))
    end = time.time()
    print(f'Intersection executed in {(end - start) * 1000} milliseconds')

    print("============== TEST ENDED ==============\n")


# Test case 1
test_operations_time(
    values1=[3, 2, 4, 35, 6, 65, 6, 4, 3, 21],
    values2=[6, 32, 4, 9, 6, 1, 11, 21, 1]
)
# Test case 2

test_operations_time(
    values1=[3, 2, 4, 35, 6, 65, 6, 4, 3, 23],
    values2=[1, 7, 8, 9, 11, 21, 1]
)

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
test_operations_time(
    values1=[random.randint(0, 100) for _ in range(100)],
    values2=[random.randint(0, 100) for _ in range(100)]
)

# Test Case 2
test_operations_time(
    values1=[],
    values2=[]
)

# Test Case 3
test_operations_time(
    values1=[random.randint(0, 100000000) for _ in range(1000000)],
    values2=[random.randint(0, 100000000) for _ in range(1000000)]
)
