from typing import Optional


class LRUCache:
    def __init__(self, capacity: int):
        self.lruDict = dict()
        self.linkedList = DoubleLinkedList(capacity)
        self.capacity = capacity

    def get(self, key: int) -> int:
        print("Get: " + str(key))

        if key not in self.lruDict:
            print("Get returns -1")
            print("_________________")
            return -1

        node = self.lruDict[key]
        self.linkedList.move_node_to_head(node)

        print("Get returns " + str(node.value))

        self.print_all()

        return node.value

    def put(self, key: int, value: int) -> None:
        print("Put: " + str(key))

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

        self.print_all()


    def print_all(self):
        print("Head = Key: ", end='')
        print(str(self.linkedList.headNode.key) + " Value: ", end='')
        print(self.linkedList.headNode.value)

        print("Tail = Key: ", end='')
        print(str(self.linkedList.tailNode.key) + " Value: ", end='')
        print(self.linkedList.tailNode.value)

        node = self.linkedList.headNode
        for i in range(self.linkedList.elements):
            print("[" + str(node.key) + ", " + str(node.value) + "] ", end='', sep=' ')
            node = node.next

        print("")
        print("_________________")



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
        if self.headNode == node or self.elements < 2:
            return

        old_head = self.headNode
        self.headNode = node

        if self.headNode == self.tailNode:
            self.tailNode = self.tailNode.previous
            self.tailNode.next = self.headNode

        if self.tailNode.previous == self.headNode:
            self.tailNode.previous = self.headNode.previous

        old_head.previous = self.headNode
        if old_head.next == self.headNode:
            old_head.next = self.headNode.next

        self.headNode.previous = self.tailNode
        self.headNode.next = old_head

        self.tailNode.next = self.headNode

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


lru_cache = LRUCache(3)
lru_cache.put(1,1)
lru_cache.put(2,2)
lru_cache.put(3,3)
lru_cache.put(4,4)
lru_cache.get(4)
lru_cache.get(3)
lru_cache.get(2)
lru_cache.get(1)
lru_cache.put(5,5)
lru_cache.get(1)
lru_cache.get(2)
lru_cache.get(3)
lru_cache.get(4)
lru_cache.get(5)
