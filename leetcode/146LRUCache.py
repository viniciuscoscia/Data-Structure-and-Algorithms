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

        if key in self.lruDict:
            node = self.lruDict[key]
            node.value = value
            self.linkedList.move_node_to_head(node)
        else:
            node = Node(key, value)
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
        print("Head to tail:")
        for i in range(self.linkedList.elements):
            print("[" + str(node.key) + ", " + str(node.value) + "] ", end='', sep=' ')
            node = node.next

        node = self.linkedList.tailNode
        print("\nTail to head:")
        for i in range(self.linkedList.elements):
            print("[" + str(node.key) + ", " + str(node.value) + "] ", end='', sep=' ')
            node = node.previous

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

    def move_node_to_head(self, new_head: Node):
        if self.headNode == new_head:
            return

        if self.tailNode.key == new_head.key:
            if self.elements > 2:
                self.tailNode = self.tailNode.previous
                new_head.next = self.headNode
                self.headNode = new_head
                return
            else:
                self.tailNode = self.headNode
                self.headNode = new_head
                return

        old_head = self.headNode

        if old_head.next.key == new_head.key:
            old_head.next = new_head.next
            new_head.next.previous = old_head

        if self.tailNode.previous.key == new_head.key:
            self.tailNode.previous = new_head.previous

        previous = new_head.previous
        new_head.next.previous = previous
        previous.next = new_head.next

        new_head.next = old_head
        new_head.previous = self.tailNode

        old_head.previous = new_head
        self.tailNode.next = new_head
        self.headNode = new_head


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
        self.headNode.previous = self.tailNode
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



print("\n\n--------------------------- TEST 1 ---------------------------\n\n")
lru_cache = LRUCache(2)
lru_cache.put(1,1)
lru_cache.put(2,2)
lru_cache.get(1)
lru_cache.put(3,3)
lru_cache.get(2)
lru_cache.put(4,4)
lru_cache.get(1)
lru_cache.get(3)
lru_cache.get(4)

print("\n\n--------------------------- TEST 2 ---------------------------\n\n")
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

print("\n\n--------------------------- TEST 3 ---------------------------\n\n")
lru_cache = LRUCache(5)
lru_cache.put(1,1)
lru_cache.put(2,2)
lru_cache.put(3,3)
lru_cache.put(4,4)
lru_cache.put(5,5)
lru_cache.put(6,6)
lru_cache.get(1)
lru_cache.get(4)
lru_cache.get(3)
lru_cache.get(2)
lru_cache.put(6,66)
lru_cache.put(4,44)
lru_cache.get(1)
lru_cache.get(2)
lru_cache.get(3)
lru_cache.get(4)
lru_cache.get(5)

# Claude Solution
# Added sentinel nodes in the doubly linked list:
#
# Eliminates many edge cases
# Simplifies the code by removing special cases for head/tail
# Makes operations more uniform and less error-prone
#
#
# Improved code organization and separation of concerns:
#
# Split list operations into clear, single-purpose methods
# Removed redundant state tracking
# Better encapsulation of internal operations
#
#
# Added type hints and documentation:
#
# Comprehensive docstrings explaining purpose and behavior
# Type hints for better code maintainability
# Clear parameter and return value documentation
#
#
# Simplified the node movement logic:
#
# Removed complex conditional branches
# Made operations more atomic and easier to understand
# Eliminated redundant checks
#
#
# Added error handling:
#
# Validates capacity in constructor
# More robust handling of edge cases
#
#
# Improved variable naming:
#
# More descriptive names (e.g., prev instead of previous)
# Consistent naming conventions
# Clear abbreviations (e.g., dll for doubly linked list)
#
#
# Memory management improvements:
#
# Better cleanup of references when removing nodes
# Clearer ownership of nodes between cache and list
class Node:
    """A node in the doubly linked list containing key-value pairs."""

    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None


class DoubleLinkedList:
    """A doubly linked list implementation for the LRU cache."""

    def __init__(self):
        # Use sentinel nodes to simplify edge cases
        self.head = Node(0, 0)  # Sentinel head
        self.tail = Node(0, 0)  # Sentinel tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_to_front(self, node: Node) -> None:
        """Add a node right after the head sentinel."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove_node(self, node: Node) -> None:
        """Remove a node from the linked list."""
        prev_node = node.prev
        next_node = node.next
        if prev_node and next_node:
            prev_node.next = next_node
            next_node.prev = prev_node
        self.size -= 1

    def remove_last(self) -> Optional[Node]:
        """Remove and return the last node before the tail sentinel."""
        if self.size == 0:
            return None
        last = self.tail.prev
        if last:
            self.remove_node(last)
            return last
        return None


class LRUCache:
    """
    A Least Recently Used (LRU) cache implementation using a hash map and doubly linked list.

    The hash map provides O(1) lookup while the doubly linked list maintains the order
    of elements based on their access time.
    """

    def __init__(self, capacity: int):
        """Initialize LRU cache with given capacity."""
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self.capacity = capacity
        self.cache = {}  # Hash map for O(1) lookup
        self.dll = DoubleLinkedList()

    def _move_to_front(self, node: Node) -> None:
        """Move an existing node to the front of the list."""
        self.dll.remove_node(node)
        self.dll.add_to_front(node)

    def get(self, key: int) -> int:
        """
        Retrieve value by key and move it to front (most recently used position).
        Returns -1 if key doesn't exist.
        """
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._move_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """
        Insert or update key-value pair. If key exists, update value and move to front.
        If cache is full, remove least recently used item before inserting new one.
        """
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
            return

        new_node = Node(key, value)
        self.cache[key] = new_node
        self.dll.add_to_front(new_node)

        if len(self.cache) > self.capacity:
            last_node = self.dll.remove_last()
            if last_node:
                del self.cache[last_node.key]