from udacity.data_structures.stack.exercises.reverse_polish_notation.Stack import Stack
import operator


def evaluate_post_fix(input_list):
    """
    Evaluate the postfix expression to find the answer

    Args:
       input_list(list): List containing the postfix expression
    Returns:
       int: Postfix expression solution
    """

    stack = Stack()

    ops = {"+": operator.add, "-": operator.sub, "/": operator.truediv, "*": operator.mul}

    for char in input_list:
        if char in ops:
            first_number = int(stack.pop())
            second_number = int(stack.pop())

            result = int(ops[char](second_number, first_number))

            stack.push(result)
        else:
            stack.push(char)

    return stack.pop()


def test_function(test_case):
    output = evaluate_post_fix(test_case[0])
    print(output)
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")


test_case_1 = [["3", "1", "+", "4", "*"], 16]
test_function(test_case_1)

test_case_2 = [["4", "13", "5", "/", "+"], 6]
test_function(test_case_2)

test_case_3 = [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22]
test_function(test_case_3)
