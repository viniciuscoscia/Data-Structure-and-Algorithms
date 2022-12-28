from udacity.data_structures.tree.binary_search_tree.BinarySearchTree import BinarySearchTree

tree = BinarySearchTree()
tree.insert_with_recursion(5)
tree.insert_with_recursion(6)
tree.insert_with_recursion(4)
tree.insert_with_recursion(2)
tree.insert_with_recursion(5) # insert duplicate
print(tree)
