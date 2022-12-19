from udacity.data_structures.linked_list.Node import Node
from udacity.data_structures.linked_list.linked_list import LinkedList


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


def reverse(linked_list: LinkedList) -> LinkedList:
    reversed_linked_list = LinkedList()
    previous_node = None

    for value in linked_list:
        new_node = Node(value)
        new_node.next = previous_node
        previous_node = new_node

    reversed_linked_list.head = previous_node
    return reversed_linked_list

