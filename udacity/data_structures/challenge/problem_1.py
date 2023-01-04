from typing import Optional


class DoubleLinkedNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class LRUCache:

    def __init__(self, capacity):
        self.hash_table = dict()
        self.capacity = capacity
        self.counter = 0
        self.head = None
        self.tail = None

    # Returns -1 if node not found
    def get(self, key):
        if key is None:
            return -1

        node = self.hash_table.get(key)

        if node is None:
            return -1

        if self.tail == node:
            return node.value

        self.unlink_node(node)
        self.set_tail(node)

        return node.value

    def set(self, key, value):
        if key is None:
            return

        node = self.hash_table.get(key)

        if node is not None:
            node.value = value
            self.move_node_to_tail(node)
            return

        new_node = DoubleLinkedNode(key, value)
        self.hash_table[key] = new_node
        self.set_tail(new_node)
        self.increment_counter()

        self.check_cache_limit()

    def move_node_to_tail(self, node):
        if self.tail != node:
            self.unlink_node(node)
            self.set_tail(node)

    def check_cache_limit(self):
        if self.is_cache_full():
            self.hash_table.pop(self.decapitate().key)
            self.decrement_counter()

    def is_cache_full(self):
        return self.counter > self.capacity

    def unlink_node(self, node: DoubleLinkedNode):
        if self.head == node:
            self.decapitate()
            return

        if self.tail == node:
            self.cut_tail()
            return

        next_node, previous_node = node.next, node.previous

        next_node.previous = previous_node
        previous_node.next = next_node

    # Removes HEAD on DoubleLinkedList
    # Returns old head Node or None if cache is empty
    def decapitate(self) -> Optional[DoubleLinkedNode]:
        if self.head is None:
            return None

        old_head = self.head
        new_head = old_head.next

        old_head.next = None

        if new_head is None:
            self.clear_cache()
            return old_head

        new_head.previous = None

        self.head = new_head

        return old_head

    def set_tail(self, node: DoubleLinkedNode):
        if self.tail is None:
            self.tail = node
            self.head = node
            return

        old_tail = self.tail
        old_tail.next = node
        node.previous = old_tail
        node.next = None
        self.tail = node

    def cut_tail(self) -> Optional[DoubleLinkedNode]:
        if self.tail is None:
            return None

        old_tail = self.tail
        new_tail = old_tail.previous

        old_tail.previous = None

        if new_tail is None:
            self.clear_cache()
            return old_tail

        new_tail.next = None

        self.tail = new_tail

        return old_tail

    def clear_cache(self):
        self.head = None
        self.tail = None
        self.counter = 0
        self.hash_table = dict()

    def increment_counter(self):
        self.counter += 1

    def decrement_counter(self):
        self.counter -= 1


our_cache = LRUCache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
our_cache.set(3, 33)
print(our_cache.get(3))  # 33

our_cache.set(5, 55)
print(our_cache.get(5))  # 55

our_cache.set(None, 1000)
print(our_cache.get(None))  # Skip

# Test Case 2
our_cache.set(6, None)
print(our_cache.get(6))  # None

# Test Case 3
our_cache.set(1, 100000000000000000000000000000000000000000000)
print(our_cache.get(1))  #100000000000000000000000000000000000000000000

print(our_cache.hash_table)
