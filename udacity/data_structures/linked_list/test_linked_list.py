from udacity.data_structures.linked_list.linked_list import LinkedList
from udacity.data_structures.linked_list.linked_list_utils import reverse

llist = LinkedList()
for value in [4, 2, 5, 1, -3, 0]:
    llist.append(value)

flipped = reverse(llist)
is_correct = list(flipped) == list([0, -3, 1, 5, 2, 4]) and list(llist) == list(reverse(flipped))
print("Pass" if is_correct else "Fail")
