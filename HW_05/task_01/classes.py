class MyClass:
    """test class"""
    def __init__(self, value):
        self.value = value

    def say_hello(self):
        return f"Hello, {self.value}"


class AnotherClass:
    """test class 2"""
    class_attr = 42

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self):
        return self.x + self.y

    @staticmethod
    def static_method():
        return "static"

    @classmethod
    def class_method(cls):
        return f"method from {cls.__name__}"
