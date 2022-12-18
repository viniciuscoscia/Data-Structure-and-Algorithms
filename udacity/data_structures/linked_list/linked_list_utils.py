from udacity.data_structures.linked_list.Node import Node


def print_linked_list(head):
    current_node = head

    while current_node:
        print(current_node.value)
        current_node = current_node.next


def create_linked_list(values):
    head = None
    current_node = None
    for value in values:
        if head is None:
            head = Node(value)
            current_node = head
        else:
            current_node.next = Node(value)
            current_node = current_node.next
    return head
