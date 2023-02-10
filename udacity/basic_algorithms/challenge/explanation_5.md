    As proposed in this problem, it uses a trie data structure to solve it.
Tries are data structures with multiple children, allowing us to build a structure for the autocomplete function by
having nodes with other nodes. Each node represents a character and has a flag to mark if the char is the end of a word.
    The insertion operation into the Trie is a Linear Time O(n), where "n" is the size of the word to add to the dictionary.
The bigger the word, the more nodes it needs to be added, iterating through the word.
The best case for this operation is adding one character, and the worst is adding the longest word ever known, which is "pneumonoultramicroscopicsilicovolcanoconiosis." Also, this is a Linear Space operation O(m) where "m" is the extra nodes added, as we don't add new nodes if it already exists, for example, if we create a new Trie and add "ant," we're adding three nodes to the Data Structure. Then, we add "anthology", only the nodes for "hology" will need to be created.
    The search operation "Trie.find" is a Linear Time Complexity operation O(n), where is the length of the word to be searched,
and Linear Space Complexity O(m). For this operation, we iterate through each char of the word searching for nodes in the Trie,
then using recursion. Worst and best case scenarios are based on the length of the suffix and how many words we have
available in our dictionary to autocomplete.