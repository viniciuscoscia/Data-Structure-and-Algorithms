class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    '''
    Adds a new node with the value in the argument and returns it's reference.
    '''
    def add_next_value(self, value):
        node = Node(value)
        self.next = node
        return node

