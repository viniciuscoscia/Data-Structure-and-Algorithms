from collections import defaultdict

from ipywidgets import interact


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

    def insert(self, char):
        return self.children[char]

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for
        # all complete words below this point

        suffixes = []

        node = self
        for char in suffix:
            node = node.children.get(char, None)
            if node is None:
                break

        def find_suffixes(node: TrieNode, word: str):
            if node.is_word:
                suffixes.append(word)

            for key, child_node in node.children.items():
                find_suffixes(child_node, word=word + key)

        find_suffixes(node, "")

        return suffixes


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Add `word` to trie
        """
        current_node = self.root

        for char in word:
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return False

            current_node = current_node.children[char]

        return current_node


trie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    trie.insert(word)


def f(prefix):
    if prefix != '':
        prefix_node = trie.find(prefix)
        if prefix_node:
            print('\n'.join(prefix_node.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')


# Tests

interact(f, prefix='a')
# nt
# nthology
# ntagonist
# ntonym


interact(f, prefix='fa')
# ctory


interact(f, prefix='fa')
# ctory

interact(f, prefix='t')
# rie
# rigger
# rigonometry
# ripod

interact(f, prefix='tr')
# rie
# rigger
# rigonometry
# ripod


interact(f, prefix='')  # Nothing happens
interact(f, prefix='asdasd') # asdasd not found
