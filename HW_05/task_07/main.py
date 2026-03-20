from typing import Any, Callable


def log_methods(cls: type) -> type:
    """Class decorator"""
    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value):

            def outer(method: Callable, name: str) -> Callable:
                """Adds logging before calling the original method"""

                def inner(self, *args: Any, **kwargs: Any) -> Any:
                    """
                    Function that logs the method call
                    and then calls the original method
                    """
                    print(f"Logging: {name} called with {args}")

                    return method(self, *args, **kwargs)

                return inner

            setattr(cls, attr_name, outer(attr_value, attr_name))
    return cls


@log_methods
class MyClass:
    """Summ two numbers"""
    def add(self, a: int, b: int) -> int:
        return a + b

    def subtract(self, a: int, b: int) -> int:
        """Substract two numbers"""
        return a - b


if __name__ == "__main__":
    obj = MyClass()
    obj.add(5, 3)
    obj.subtract(5, 3)
