from typing import Callable


def memoize(func: Callable):
    """
    Decorator that caches results in a dictionary
    where the key is the function arguments and the value
    is the result returned by the function for those arguments
    """
    cache: dict = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper


@memoize
def fib(n: int) -> int:
    """Calculation of the Fibonacci sequence"""

    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


@memoize
def factorial(n: int) -> int:
    """Calculates the factorial of n"""
    if n == 0:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    print(fib(20))
    print(fib(22))
    print(factorial(300))
