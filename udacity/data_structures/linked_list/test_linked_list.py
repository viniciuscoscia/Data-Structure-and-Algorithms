from udacity.data_structures.linked_list.linked_list import LinkedList
from udacity.data_structures.linked_list.linked_list_utils import is_circular

# Test Cases
list_with_loop = LinkedList([2, -1, 3, 0, 5])

# Creating a loop where the last node points back to the second node
loop_start = list_with_loop.head.next

node = list_with_loop.head
while node.next:
    node = node.next
node.next = loop_start

# Create another circular linked list
small_loop = LinkedList([0])
small_loop.head.next = small_loop.head

print("Pass" if is_circular(list_with_loop) else "Fail")  # Pass
print("Pass" if is_circular(LinkedList([-4, 7, 2, 5, -1])) else "Fail")  # Fail
print("Pass" if is_circular(LinkedList([1])) else "Fail")  # Fail
print("Pass" if is_circular(small_loop) else "Fail")  # Pass
print("Pass" if is_circular(LinkedList([])) else "Fail")  # Fail
