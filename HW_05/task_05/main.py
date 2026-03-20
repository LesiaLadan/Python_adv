class MutableClass:
    """
    Class allows dynamic modification of its attributes
    """

    def add_attr(self, name: str, value: object) -> None:
        """
        Dynamically adds an attribute to the object
        """
        setattr(self, name, value)

    def delete_attr(self, name: str) -> None:
        """
        Dynamically removes an attribute from the object if it exists
        """
        if hasattr(self, name):
            delattr(self, name)


if __name__ == "__main__":
    obj = MutableClass()

    obj.add_attr("name", "Python")
    print(obj.name)

    obj.delete_attr("name")

    # print(obj.name)
