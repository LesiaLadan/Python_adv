from typing import Any


class SingletonMeta(type):
    """Metaclass that ensures a class has only one instance"""

    instances = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        """Control of instance creation"""
        if cls not in cls.instances:
            cls.instances[cls] = super().__call__(*args, **kwargs)
        return cls.instances[cls]


class Singleton(metaclass=SingletonMeta):
    """Example singleton class"""

    def __init__(self) -> None:
        print("Creating instance")


if __name__ == "__main__":
    obj1 = Singleton()
    obj2 = Singleton()
    obj3 = obj2

    print(obj1 is obj2)
    print(obj1 is obj3)
