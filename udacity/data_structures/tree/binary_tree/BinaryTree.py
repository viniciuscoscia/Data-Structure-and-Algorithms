from __future__ import annotations

from udacity.data_structures.tree.binary_tree.NodeState import NodeState
from udacity.data_structures.tree.binary_tree.TreeNode import TreeNode
from udacity.data_structures.tree.binary_tree.TreeStack import TreeStack


class BinaryTree:
    def __init__(self, value=None):
        self.__root = TreeNode(value)

    def get_root(self):
        return self.__root

    def pre_order_traversal_with_recursion(self):
        visit_order = list()

        def traverse(node):
            if node:
                # visit the node
                visit_order.append(node.get_value())

                # traverse left subtree
                traverse(node.get_left_child())

                # traverse right subtree
                traverse(node.get_right_child())

        traverse(self.get_root())

        return visit_order

