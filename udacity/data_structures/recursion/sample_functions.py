def power_of_2(n):
    if n == 0:
        return 1

    return 2 * power_of_2(n - 1)


def sum_integers(n):
    if n == 1:
        return n
    return n + sum_integers(n - 1)


def factorial(n):
    """
    Calculate n!

    Args:
       n(int): factorial to be computed
    Returns:
       n!
    """
    if n <= 1:
        return 1

    return n * factorial(n - 1)


print("Pass" if (1 == factorial(0)) else "Fail")
print("Pass" if (1 == factorial(1)) else "Fail")
print("Pass" if (120 == factorial(5)) else "Fail")
