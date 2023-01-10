basic_trie = {
    # a and add word
    'a': {
        'd': {
            'd': {
                'word_end': True},
            'word_end': False},
        'word_end': True},
    # hi word
    'h': {
        'i': {'word_end': True},
        'word_end': False}}


print('Is "a"   a word: {}'.format(basic_trie['a']['word_end']))
print('Is "ad"  a word: {}'.format(basic_trie['a']['d']['word_end']))
print('Is "add" a word: {}'.format(basic_trie['a']['d']['d']['word_end']))


def is_word(word):
    """
    Look for the word in `basic_trie`
    """
    current_node = basic_trie

    for char in word:
        if char not in current_node:
            return False

        current_node = current_node[char]

    return current_node['word_end']


# Test words
test_words = ['ap', 'add', "h", "hi"]
for word in test_words:
    if is_word(word):
        print('"{}" is a word.'.format(word))
    else:
        print('"{}" is not a word.'.format(word))