from udacity.data_structures.tree.binary_tree.BinaryTree import BinaryTree
from udacity.data_structures.tree.binary_tree.TreeNode import TreeNode
from udacity.data_structures.tree.binary_tree.TreeStack import TreeStack
from udacity.data_structures.tree.binary_tree.binary_tree_search import depth_first_search


#
#
# tree = BinaryTree("apple")  # root node
#
# tree.get_root().set_left_child(TreeNode("banana"))
# tree.get_root().get_left_child().set_left_child(TreeNode("dates"))
#
# tree.get_root().set_right_child(TreeNode("cherry"))
#
# visit_order = list()
# stack = TreeStack()
#
# node = tree.get_root()
# stack.push(node)
#
# print(f"""
# visit_order {visit_order}
# stack:
# {stack}
# """)
#
# visit_order.append(node.get_value())
# print(f"""visit order {visit_order}
# {stack}
# """)
#
# print(f"{node} has left child? {node.has_left_child()}")
#
# if node.has_left_child():
#     node = node.get_left_child()
#     stack.push(node)
#
# print(f"""
# visit_order {visit_order}
# stack:
# {stack}
# """)
#
# # visit banana (first level's left child)
# print(f"visit {node}")
# visit_order.append(node.get_value())
# print(f"""visit_order {visit_order}""")
#
# # check if banana has a left child (second level's left chile)
# print(f"{node} has left child? {node.has_left_child()}")
#
# # since banana has a left child "dates"
# # we'll visit "dates" and add it to the stack
# if node.has_left_child():
#     node = node.get_left_child()
#     stack.push(node)
#
# print(f"""
# visit_order {visit_order}
# stack:
# {stack}
# """)
#
# # visit dates (second level's left chile)
# visit_order.append(node.get_value())
# print(f"visit order {visit_order}")
#
# # check if "dates" has a left child -> return boolean value
# print(f"{node} has left child? {node.has_left_child()}")
#
# # since dates doesn't have a left child, we'll check if it has a right child
# print(f"{node} has right child? {node.has_right_child()}")


tree = BinaryTree(100)

tree.get_root().set_left_child(TreeNode(75))
tree.get_root().get_left_child().set_left_child(TreeNode(50))
tree.get_root().get_left_child().set_right_child(TreeNode(80))

tree.get_root().set_right_child(TreeNode(150))

depth_first_search(tree)