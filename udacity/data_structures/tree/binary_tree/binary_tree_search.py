from udacity.data_structures.tree.binary_tree.BinaryTree import BinaryTree
from udacity.data_structures.tree.binary_tree.NodeState import NodeState
from udacity.data_structures.tree.binary_tree.TreeStack import TreeStack


def depth_first_search(tree: BinaryTree):
    stack = TreeStack()
    root_state = NodeState(tree.get_root())
    stack.push(root_state)

    visit_order = list()
    visit_order.append(root_state.node.value)

    __recursive_search(stack, visit_order)

    print(visit_order)


def __recursive_search(stack: TreeStack, visit_order: list):
    print(stack)
    state = stack.top()
    if state.node.has_left_child() and not state.visited_left:
        state.visited_left = True

        left_state = NodeState(state.node.get_left_child())
        stack.push(left_state)

        visit_order.append(left_state.node.value)
        __recursive_search(stack, visit_order)
    elif state.node.has_right_child() and not state.visited_right:
        state.visited_right = True

        right_state = NodeState(state.node.get_right_child())
        stack.push(right_state)

        visit_order.append(right_state.node.value)
        __recursive_search(stack,  visit_order)
    else:
        print(stack.pop())
        if not stack.is_empty():
            stack.top()
            __recursive_search(stack, visit_order)
        else:
            return

