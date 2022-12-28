from udacity.data_structures.tree.binary_tree.TreeNode import TreeNode


class NodeState:
    def __init__(self, node: TreeNode):
        self.node = node
        self.visited_left = False
        self.visited_right = False

    def __repr__(self):
        s = f"""{self.node}
visited_left: {self.visited_left}
visited_right: {self.visited_right}
        """
        return s
