def analyze_inheritance(cls) -> None:
    """
    Prints methods inherited from base classes
    """
    print(f"Class {cls.__name__} inherited:\n ")
    for base in cls.__bases__:
        methods = []
        for attr_name, attr_value in base.__dict__.items():
            if callable(attr_value) and not attr_name.startswith("__"):
                methods.append(attr_name)
        if methods:
            print(f"- {', '.join(methods)} from {base.__name__}")
        else:
            print(f"- no methods from {base.__name__}")


class Parent:
    def parent_method(self):
        """test method"""
        pass

    def parent_method_2(self):
        """test method"""
        pass

    # pass


class Child(Parent):
    """test method"""

    def child_method(self):
        pass


if __name__ == "__main__":
    analyze_inheritance(Child)
