from udacity.data_structures.linked_list.Node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return

    def to_list(self):
        items = list()
        current_node: Node = self.head

        while current_node:
            items.append(current_node.value)
            current_node = current_node.next

        return items
