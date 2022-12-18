from udacity.data_structures.double_linked_list.DoubleNode import DoubleNode


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        head: DoubleNode = self.head
        current_tail: DoubleNode = self.tail
        new_tail = DoubleNode(value)

        if head is None:
            self.head = new_tail
            self.tail = new_tail
            return

        new_tail.previous = current_tail
        current_tail.next = new_tail
        self.tail = new_tail
