from typing import Any
from classes import Calculator, AnotherClass


def call_function(obj, method_name, *args) -> Any:
    """"Call specified object method"""
    try:
        if not hasattr(obj, method_name):
            raise AttributeError(f"{method_name} not found")
        method = getattr(obj, method_name)
        if not callable(method):
            raise TypeError(f"{method_name} is not callable")
        return method(*args)
    except AttributeError as err:
        return err
    except TypeError as err:
        return err


if __name__ == "__main__":

    calc = Calculator()
    print(call_function(calc, "a", 10, 5))
    print(call_function(calc, "b", 1, 2))
    print(call_function(calc, "add", 10, 5))
    print(call_function(calc, "subtract", 20, 5))

    another_class = AnotherClass(2, 3)
    print(call_function(another_class, "sum"))
    print(call_function(another_class, "sum"))
