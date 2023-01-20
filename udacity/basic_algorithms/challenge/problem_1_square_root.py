# Newton-Raphson Method
def try_guess(guess: int, input: int):
    result = guess * guess

    if result == input:
        return guess
    elif result > input:
        smaller_guess = guess - 1

        if smaller_guess * smaller_guess <= input:  # If input is between result and smaller result, returns smaller
            # (floor)
            return smaller_guess
        else:
            return try_guess(guess=(guess // 2) - 1, input=input)
    else:
        bigger_guess = guess + 1

        if bigger_guess * bigger_guess > input:
            return guess
        else:
            return try_guess(guess=(guess * 2) + 1, input=input)


def sqrt(input: int):
    """
    Calculate the floored square root of a number

    Args:
       input(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if input is None or input < 1:
        return 0

    return try_guess(guess=input // 2, input=input)


print("TEST 1")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (2 == sqrt(4)) else "Fail")
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (3 == sqrt(15)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (5 == sqrt(25)) else "Fail")
print("Pass" if (6 == sqrt(36)) else "Fail")
print("Pass" if (10 == sqrt(100)) else "Fail")

print("TEST 2")  # Test floor results
print("Pass" if (5 == sqrt(30)) else "Fail")
print("Pass" if (6 == sqrt(37)) else "Fail")
print("Pass" if (10 == sqrt(110)) else "Fail")

print("TEST 3")  # Edge Cases
print("Pass" if (0 == sqrt(None)) else "Fail")
print("Pass" if (0 == sqrt(0.1)) else "Fail")
print("Pass" if (0 == sqrt(-10)) else "Fail")
