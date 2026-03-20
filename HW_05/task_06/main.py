from typing import Any, Callable


class Proxy:
    """Class that intercepts method calls to another object"""
    def __init__(self, obj: Any) -> None:
        """Initialize the proxy with the target object"""
        self.obj = obj

    def __getattr__(self, name: str) -> Callable:
        """
        Intercept attribute access and wrap callable attributes to log calls
        """
        atr = getattr(self.obj, name)

        def inner_function(*args: Any, **kvargs: Any) -> Any:

            print(f"calling method:\n {name} with arguments: {args}")
            return atr(*args, **kvargs)

        return inner_function


class MyClass:
    """Test class"""
    def greet(self, name: str) -> str:
        """Greet a person by name"""
        return f"Hello, {name}!"

    def see_you(self, name: str, when: str) -> str:
        """Say goodbye to a person"""
        return f"By, {name}, see you {when}!"


if __name__ == "__main__":

    obje = MyClass()
    proxy = Proxy(obje)

    print(proxy.greet("Alise"))
    print(proxy.see_you("Ann", "tomorrow"))
