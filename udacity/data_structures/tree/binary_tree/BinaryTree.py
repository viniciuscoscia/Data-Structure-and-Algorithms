from udacity.data_structures.tree.binary_tree.TreeNode import TreeNode
from udacity.data_structures.tree.binary_tree.TreeStack import TreeStack


class BinaryTree:
    def __init__(self, value=None):
        self.__root = TreeNode(value)

    def get_root(self):
        return self.__root
