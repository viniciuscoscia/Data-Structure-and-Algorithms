from udacity.data_structures.tree.binary_search_tree.TreeQueue import Queue
from udacity.data_structures.tree.binary_tree.TreeNode import TreeNode


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = TreeNode(value)

    def get_root(self):
        return self.root

    """
    define insert here
    can use a for loop (try one or both ways)
    """

    def insert_with_loop(self, new_value):
        # ADD YOUR CODE HERE
        pass

    """
    define insert here (can use recursion)
    try one or both ways
    """

    def insert_with_recursion(self, value):
        root = self.get_root()
        if root is None:
            self.set_root(value)
            return

        new_node = TreeNode(value)

        def insert(node: TreeNode):
            if node.get_value() < value:
                if node.has_right_child():
                    insert(node.get_right_child())
                else:
                    node.set_right_child(new_node)
            elif node.get_value() > value:
                if node.has_left_child():
                    insert(node.get_left_child())
                else:
                    node.set_left_child(new_node)
            else:
                node = new_node
                return

        insert(root)

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq((node, level))
        while len(q) > 0:
            node, level = q.deq()
            if node is None:
                visit_order.append(("<empty>", level))
                continue
            visit_order.append((node, level))
            if node.has_left_child():
                q.enq((node.get_left_child(), level + 1))
            else:
                q.enq((None, level + 1))

            if node.has_right_child():
                q.enq((node.get_right_child(), level + 1))
            else:
                q.enq((None, level + 1))

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level

        return s


def compare(self, node, new_node):
    """
    0 means new_node equals node
    -1 means new node less than existing node
    1 means new node greater than existing node
    """
    if new_node.get_value() == node.get_value():
        return 0
    elif new_node.get_value() < node.get_value():
        return -1
    else:
        return 1