from classes import MyClass, AnotherClass
from typing import Any


def analyze_object(obj: Any) -> None:
    """
    Analyze a Python object and print information:
     - The type of the object
     - A list of all attributes and methods
     - The type of each attribute and method
    """
    print(type(obj))
    print(dir(obj))
    for name in dir(obj):
        if name.startswith("__"):
            continue
        attr = getattr(obj, name)
        print(f"{name}: {type(attr)}")


if __name__ == "__main__":
    obj1 = MyClass("World")
    obj2 = AnotherClass(3, 5)

    analyze_object(obj1)
    print("-" * 30)
    analyze_object(obj2)
    print("-" * 30)
    analyze_object(2)
    print("-" * 30)
    analyze_object(float)
