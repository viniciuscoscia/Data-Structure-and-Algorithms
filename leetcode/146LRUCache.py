from typing import Optional


class LRUCache:
    def __init__(self, capacity: int):
        self.lruDict = dict()
        self.linkedList = DoubleLinkedList(capacity)
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.lruDict:
            return -1

        node = self.lruDict[key]
        self.linkedList.move_node_to_head(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key in self.lruDict:
            node = self.lruDict[key]
            node.value = value
            self.linkedList.move_node_to_head(node)
        else:
            removed_node = self.linkedList.insert_front(node)
            if removed_node:
                self.lruDict.pop(removed_node.key)
            self.lruDict[key] = node


class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class DoubleLinkedList:
    def __init__(self, capacity: int):
        self.headNode: Optional[Node] = None
        self.tailNode: Optional[Node] = None
        self.capacity = capacity
        self.elements = 0

    def move_node_to_head(self, node: Node):
        old_head = self.headNode
        self.headNode = node

        old_head.previous = self.headNode
        self.headNode.next = old_head

        if node == self.tailNode:
            self.tailNode = node.previous

    '''
    Returns Last Node Tail if limit is reached
    '''

    def insert_front(self, node: Node) -> [Node]:
        if not self.headNode:
            self.headNode = node
            self.tailNode = node
            node.previous = node
            node.next = node
            self.elements += 1
            return None

        old_head = self.headNode
        old_head.previous = node

        self.headNode = node
        node.next = old_head

        if self.elements < self.capacity:
            self.tailNode.next = node
            self.elements += 1
            return None

        if self.elements == self.capacity:
            removed_tail = self.tailNode
            self.tailNode = removed_tail.previous
            self.tailNode.next = self.headNode
            self.headNode.previous = self.tailNode
            return removed_tail

    def is_full_capacity(self) -> bool:
        return self.capacity == self.elements


lRUCache = LRUCache(2)
lRUCache.put(2, 1)
lRUCache.put(2, 2)
lRUCache.get(2)
lRUCache.put(1, 1)
lRUCache.put(4, 1)
lRUCache.get(2)