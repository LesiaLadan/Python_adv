from typing import Any


class DynamicProperties:
    """Class that allows dynamic creation of properties in runtime"""

    def __init__(self) -> None:
        """Initialize storage for dynamic properties"""
        self._values = {}

    def add_property(self, name: str, default_value: Any = None) -> None:
        """Add a property with a default value"""
        self._values[name] = default_value

        def getter(self) -> Any:
            """Get property value"""
            return self._values[name]

        def setter(self, value: Any) -> None:
            """Set property value"""
            self._values[name] = value

        prop = property(getter, setter)
        setattr(self.__class__, name, prop)


if __name__ == "__main__":
    obj = DynamicProperties()
    obj.add_property("name", "default_name")

    print(obj.name)

    obj.name = "Python"
    print(obj.name)
