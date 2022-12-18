from udacity.data_structures.linked_list.linked_list import LinkedList

# Test your method here
linked_list = LinkedList()
linked_list.append(3)
linked_list.append(2)
linked_list.append(-1)
linked_list.append(0.2)

print("Pass" if (linked_list.to_list() == [3, 2, -1, 0.2]) else "Fail")
