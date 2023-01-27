TrieNode.insert(char):
    It is O(1) in both time and space complexity, simple insertion into dict.

TrieNode.suffixes(str):
    This is a linear time operation O(n). First, we iterate through the suffix and then search for words using
    recursion.
    Also, this is a Linear Space operation o(n), as it adds found words to a list and then returns it.

Trie.insert(char):
    Linear time and space complexity O(n) as we iterate through the word and make additions to the dictionary for each
    character, which is an O(1) operation

Trie.find(prefix):
    Linear Time complexity o(n) to find, iterating through the word
    Constant space complexity O(1), no new collections are required