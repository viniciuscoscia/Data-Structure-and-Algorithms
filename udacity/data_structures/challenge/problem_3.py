import sys
from functools import total_ordering
from queue import PriorityQueue


@total_ordering
class Node:
    def __init__(self, value=None, frequency=None, right_child=None, left_child=None):
        self.value = value
        self.frequency = frequency
        self.right_child = right_child
        self.left_child = left_child

    def is_leaf(self):
        return self.right_child is None and self.left_child is None

    def get_child_by_zero_or_one(self, number):
        if number == "0":
            return self.left_child
        elif number == "1":
            return self.right_child
        else:
            return None

    def __lt__(self, other):
        return self.frequency < other.frequency


def huffman_encoding(text_to_encode: str):
    nodes = dict()

    for char in text_to_encode:
        if char not in nodes:
            nodes[char] = Node(value=char, frequency=1)
        else:
            nodes.get(char).frequency += 1

    priority_queue = PriorityQueue()
    for char, node in nodes.items():
        priority_queue.put(node)

    while priority_queue.qsize() > 1:
        leaf_1: Node = priority_queue.get()
        leaf_2: Node = priority_queue.get()

        node = Node(
            value=leaf_1.value + leaf_2.value,
            frequency=leaf_1.frequency + leaf_2.frequency,
            left_child=leaf_1,
            right_child=leaf_2
        )

        priority_queue.put(node)

    tree_root: Node = priority_queue.get()

    code_table = build_code_table(tree_root)

    encoded = ""
    for char in text_to_encode:
        encoded += code_table.get(char)

    print(code_table)

    return encoded, tree_root


def build_code_table(huffman_tree):
    huffman_codes = dict()

    def generate_code(node: Node, code: str):
        if node.is_leaf():
            huffman_codes.setdefault(node.value, code)
            return

        generate_code(node.left_child, code + "0")
        generate_code(node.right_child, code + "1")

    generate_code(huffman_tree, "")

    return huffman_codes


def huffman_decoding(encoded_text, tree: Node):
    decoded_text = ""

    def search_character(node: Node, encoded_text):
        if node.is_leaf():
            decoded_text += node.value
            return

        char = encoded_text[0]

        if char == "0":
            return search_character(node.left_child, encoded_text[1:])
        elif char == "1":
            return search_character(node.right_child, encoded_text[1:])

    search_character(tree, encoded_text)


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1

# Test Case 2

# Test Case 3
