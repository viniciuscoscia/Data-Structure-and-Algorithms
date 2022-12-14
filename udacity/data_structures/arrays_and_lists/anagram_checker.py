def string_to_sorted_characters(string):
    characters = list()

    for char in str(string).lower():
        if char != ' ':
            characters.append(char)

    characters.sort()
    return characters


def anagram_checker(str1, str2):
    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string), str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """
    return string_to_sorted_characters(str1) == string_to_sorted_characters(str2)


print("Pass" if not (anagram_checker('water', 'waiter')) else "Fail")
print("Pass" if anagram_checker('Dormitory', 'Dirty room') else "Fail")
print("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print("Pass" if not (anagram_checker('A gentleman', 'Elegant men')) else "Fail")
print("Pass" if anagram_checker('Time and tide wait for no man', 'Notified madman into water') else "Fail")
