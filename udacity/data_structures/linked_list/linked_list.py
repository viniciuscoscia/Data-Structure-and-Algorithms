from udacity.data_structures.linked_list.Node import Node


class LinkedList:
    def __init__(self, init=None):
        self.head = None
        if init is list:
            for value in init:
                self.append(value)
        elif isinstance(init, Node):
            self.head = init

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def to_list(self) -> list:
        items = list()
        current_node: Node = self.head

        while current_node:
            items.append(current_node.value)
            current_node = current_node.next

        return items

    def prepend(self, value):
        self.head: Node

        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    """ Search the linked list for a node with the requested value and return the node. """

    def search(self, value):
        current_node: Node = self.head
        while current_node:
            if value == current_node.value:
                return current_node
            current_node = current_node.next

    def remove(self, value):
        current_node: Node = self.head
        previous_node = None
        while current_node:
            if value == current_node.value:
                if previous_node is None:
                    self.head = current_node.next
                else:
                    previous_node.next = current_node.next
                return

            previous_node = current_node
            current_node = current_node.next

    def pop(self):
        if self.head is None:
            return None
        old_head: Node = self.head
        self.head = self.head.next
        return old_head.value

    def insert(self, value, pos):
        new_node = Node(value)

        if pos == 0 or self.head is None:
            new_node.next = self.head
            self.head = new_node
            return

        current_node: Node = self.head
        previous_node = None
        for x in range(pos + 1):
            if current_node.next is None:
                current_node.next = Node(value)
                return
            elif pos == x:
                new_node.next = current_node
                previous_node.next = new_node
                return

            previous_node = current_node
            current_node = current_node.next

    def size(self):
        if self.head is None:
            return 0

        counter = 0
        current_node: Node = self.head

        while current_node:
            counter += 1
            current_node = current_node.next

        return counter

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])
