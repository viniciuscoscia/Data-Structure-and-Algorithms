from udacity.data_structures.linked_list.linked_list import LinkedList
from udacity.data_structures.linked_list.linked_list_utils import merge

''' In a NESTED LinkedList object, each node will be a simple LinkedList in itself'''

''' In a NESTED LinkedList object, each node will be a simple LinkedList in itself'''


class NestedLinkedList(LinkedList):
    def flatten(self):
        return self._flatten(self.head)  # <-- self.head is a node for NestedLinkedList

    '''  A recursive function '''

    def _flatten(self, node):
        # A termination condition
        if node.next is None:
            return merge(node.value, None)  # <-- First argument is a simple LinkedList

        # _flatten() is calling itself untill a termination condition is achieved
        return merge(node.value, self._flatten(node.next))  # <-- Both arguments are a simple LinkedList each