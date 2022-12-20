from udacity.data_structures.linked_list.NestedLinkedList import NestedLinkedList
from udacity.data_structures.linked_list.Node import Node
from udacity.data_structures.linked_list.linked_list import LinkedList

# First Test scenario
''' Create a simple LinkedList'''
linked_list = LinkedList(Node(1))  # <-- Notice that we are passing a Node made up of an integer
linked_list.append(3)  # <-- Notice that we are passing a numerical value as an argument in the append() function here
linked_list.append(5)

''' Create another simple LinkedList'''
second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

''' Create a NESTED LinkedList, where each node will be a simple LinkedList in itself'''
nested_linked_list = NestedLinkedList(Node(linked_list))  # <-- Notice that we are passing a Node made up of a simple
# LinkedList object
nested_linked_list.append(second_linked_list)  # <-- Notice that we are passing a LinkedList object in the append()
# function here

solution = nested_linked_list.flatten().to_list()  # <-- returns A LinkedList object

expected_list = [1, 2, 3, 4, 5]  # <-- Python list
# Convert the "solution" into a Python list and compare with another Python list
assert solution.to_list() == expected_list, f"list contents: {solution.to_list()}"
