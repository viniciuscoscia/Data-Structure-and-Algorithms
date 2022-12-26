from udacity.data_structures.stack.LinkedListStack.Node import Node


class LinkedListStack:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):
        new_value = Node(value)
        self.num_elements += 1

        if self.head is None:
            self.head = new_value
            return

        new_value.next = self.head
        self.head = new_value

    def pop(self):
        if self.is_empty():
            return

        old_head = self.head
        self.head = self.head.next
        self.num_elements -= 1

        return old_head

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

