import sys
from functools import total_ordering
from queue import PriorityQueue
import sys

sys.setrecursionlimit(30000)
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
    if len(text_to_encode) == 0:
        return "", Node()

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


def huffman_decoding(encoded_text: str, tree: Node):
    characters = []

    def search_character(encoded_text, node: Node):
        if node.is_leaf():
            characters.append(node.value)
            if len(encoded_text) > 0:
                return search_character(encoded_text, tree)
            else:
                return "".join(str(x) for x in characters)

        char = encoded_text[0]

        if char == "0":
            return search_character(encoded_text[1:], node.left_child)
        elif char == "1":
            return search_character(encoded_text[1:], node.right_child)

    return search_character(encoded_text, tree)


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
    a_great_sentence = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque vestibulum nisi quis purus dictum viverra. Ut quis justo porttitor, gravida metus non, iaculis tellus. In faucibus nibh hendrerit magna accumsan, a volutpat elit luctus. Vestibulum laoreet risus ac est tristique rhoncus. Integer orci erat, auctor id consequat dignissim, lobortis a lacus. Integer varius dui eu eros pretium faucibus. Fusce posuere eros at velit ultrices luctus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla viverra sit amet arcu sit amet cursus. Curabitur condimentum lectus ac quam iaculis laoreet.
Morbi molestie sed diam sit amet finibus. Sed urna lorem, feugiat non massa eu, fermentum dapibus elit. Cras vel suscipit erat. Pellentesque a ipsum lorem. Ut dui turpis, varius non mollis ut, malesuada vel dolor. Nam mi neque, lacinia at volutpat quis, condimentum at lectus. Morbi pretium turpis a lectus commodo sodales.
Phasellus at massa eleifend, facilisis enim non, pretium ipsum. Cras commodo dictum imperdiet. Pellentesque posuere vitae tellus vitae accumsan. Phasellus nulla ex, convallis eget elit et, tempor dignissim urna. Aliquam quis neque vitae nisl tempus fermentum. Pellentesque volutpat velit justo, sed pulvinar magna efficitur sit amet. Vestibulum porta orci vel felis rutrum fermentum. Nulla facilisi. Pellentesque sed metus lorem. Nunc vitae nisi erat.
Nam quis nulla nisl. Vestibulum euismod nisl libero, varius ultricies sapien interdum ut. Vestibulum tincidunt risus velit, et rutrum turpis pulvinar non. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aenean accumsan dui eu feugiat ultricies. Nullam consequat ipsum vitae sapien venenatis vulputate. Aliquam in nisl sit amet nibh malesuada molestie eleifend eget magna.
Fusce ac pretium lacus, non aliquam eros. Sed eget venenatis dui, ut tempus arcu. Suspendisse fermentum magna justo, a varius ligula vehicula nec. Morbi id ex finibus, ultrices eros vel, pellentesque felis. Aliquam gravida dui lectus, quis varius mauris sagittis eu. Suspendisse potenti. Duis ultrices nibh non arcu congue hendrerit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec consectetur lacus leo, vitae blandit odio convallis sed. Proin euismod est sapien, ut volutpat nulla vulputate non. Duis tincidunt orci vitae nisi dapibus, a ornare neque suscipit. Morbi elit diam, fringilla sed pretium vel, scelerisque non eros. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam nec tempus felis. Morbi viverra sem non aliquam sollicitudin.
"""

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # Test Case 2
    a_great_sentence = ""

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    # print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # Test Case 3
    a_great_sentence = "AAAAAAAAAAABBBBBBBBBBBBCCCCCDDEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
