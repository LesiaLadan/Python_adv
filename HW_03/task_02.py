import math
from typing import List


class Vector:
    """
    Represents a numeric-like vector
    """

    def __init__(self, coords: List[float]) -> None:
        """
        Initialize a vector with a list of coordinates\n
        - param - list of numbers representing vector lenght
        """
        self.coords = coords

    def length(self) -> float:
        """
        Return the length of the vector
        """
        return math.sqrt(sum(c**2 for c in self.coords))

    def __add__(self, other: "Vector") -> "Vector":
        """
        Add two vectors with the same lenght
        """
        if not isinstance(other, Vector):
            return NotImplemented
        if len(self.coords) != len(other.coords):
            raise ValueError("Vectors must be with the same lenght")
        new_coords = [a + b for a, b in zip(self.coords, other.coords)]
        return Vector(new_coords)

    def __mul__(self, number: int | float) -> "Vector":
        """
        Multiply the vector by a number
        """
        if not isinstance(number, (int, float)):
            return NotImplemented
        new_coords = [c * number for c in self.coords]
        return Vector(new_coords)

    def __sub__(self, other: "Vector") -> "Vector":
        """
        Subtract one vector from another
        """
        if not isinstance(other, Vector):
            return NotImplemented
        if len(self.coords) != len(other.coords):
            raise ValueError("Vectors must be with the same lenght")
        new_coords = [a - b for a, b in zip(self.coords, other.coords)]
        return Vector(new_coords)

    def __lt__(self, other: "Vector") -> bool:
        """
        Compare vectors by length - less than
        """
        if not isinstance(other, Vector):
            return NotImplemented
        return self.length() < other.length()

    def __gt__(self, other: "Vector") -> bool:
        """
        Compare vectors by length - greater than
        """
        if not isinstance(other, Vector):
            return NotImplemented
        return self.length() > other.length()

    def __eq__(self, other) -> bool:
        """
        Compare vectors by length
        """
        if not isinstance(other, Vector):
            return NotImplemented
        return self.length() == other.length()

    def __repr__(self) -> str:
        """
        Return a string-representation of the vector
        """
        return f"Vector({self.coords})"


if __name__ == "__main__":

    v1 = Vector([2, 3])
    v2 = Vector([1, 4])

    v3 = v1 + v2
    v4 = v1 - v2
    v5 = v1 * 2

    print(v3)
    print(v4)
    print(v5)

    print(v1.length())
    print(v1 < v2)
    print(v3 < v2)
    print(v1 == Vector([2, 3]))
