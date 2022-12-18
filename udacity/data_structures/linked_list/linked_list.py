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

    def to_list(self):
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
