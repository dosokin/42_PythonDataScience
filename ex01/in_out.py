def square(x: int | float) -> int | float:

    """returns the square of argument"""

    return x**2


def pow(x: int | float) -> int | float:

    """returns the
Exponentiation of argument by himself"""

    return x**x


def outer(x: int | float, function) -> object:

    """takes as argument a number
and a function, it returns an object that when called returns the
result of the arguments calculation"""

    count = 0

    def inner() -> float:
        nonlocal count
        if not count:
            count = x
        count = function(count)
        return count

    return inner
