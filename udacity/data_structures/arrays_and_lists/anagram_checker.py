def anagram_checker(str1, str2):
    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string), str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """

    first_string_characters = list()

    for char in str(str1).lower():
        if char != ' ':
            first_string_characters.append(char)

    first_string_characters.sort()

    second_string_characters = list()

    for char in str(str2).lower():
        if char != ' ':
            second_string_characters.append(char)

    second_string_characters.sort()

    return first_string_characters == second_string_characters


print("Pass" if not (anagram_checker('water', 'waiter')) else "Fail")
print("Pass" if anagram_checker('Dormitory', 'Dirty room') else "Fail")
print("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print("Pass" if not (anagram_checker('A gentleman', 'Elegant men')) else "Fail")
print("Pass" if anagram_checker('Time and tide wait for no man', 'Notified madman into water') else "Fail")
