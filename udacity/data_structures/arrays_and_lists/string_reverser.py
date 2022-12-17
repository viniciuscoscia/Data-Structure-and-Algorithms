def string_reverser(our_string):
    reversed_string = ''

    for char in our_string:
        reversed_string = f'{char}{reversed_string}'

    return reversed_string


print("Pass" if ('retaw' == string_reverser('water')) else "Fail")
print("Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser('Practicing string manipulation!')) else "Fail")
print("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser('The house code is: 2343')) else "Fail")