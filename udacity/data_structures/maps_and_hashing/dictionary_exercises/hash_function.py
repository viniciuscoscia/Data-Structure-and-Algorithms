def hash_function(string):
    hash_code = 0
    for character in string:
        hash_code += ord(character)
    return hash_code
