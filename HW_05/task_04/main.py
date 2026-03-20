from typing import Type


def create_class(class_name: str, methods: dict) -> Type:
    """Dynamically create a Python class with the given name and methods"""
    return type(class_name, (), methods)


def say_hello(self) -> str:
    return "Hello!"


def say_goodbye(self) -> str:
    return "Goodbye!"


methods = {"say_hello": say_hello, "say_goodbye": say_goodbye}

if __name__ == "__main__":

    MyDynamicClass = create_class("MyDynamicClass", methods)

    obj = MyDynamicClass()
    print(obj.say_hello())
    print(obj.say_goodbye())
