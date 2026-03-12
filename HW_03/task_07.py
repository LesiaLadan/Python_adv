import math
from typing import List


class Vector:
    """
    Represents a vector in n-dimensional space
    """

    def __init__(self, coords: List[float]) -> None:
        """
        Initialize a vector with a list of coordinates
        """
        self.coords = coords

    def length(self) -> float:
        """
        Return the length (magnitude) of the vector
        """
        return math.sqrt(sum(c**2 for c in self.coords))

    def __add__(self, other: "Vector") -> "Vector":
        """
        Add two vectors of the same size
        """
        if not isinstance(other, Vector):
            return NotImplemented
        if len(self.coords) != len(other.coords):
            raise ValueError("Vectors must have same lenght")
        new_coords = [a + b for a, b in zip(self.coords, other.coords)]
        return Vector(new_coords)

    def __sub__(self, other: "Vector") -> "Vector":
        """
        Subtract one vector from another
        """
        if not isinstance(other, Vector):
            return NotImplemented
        if len(self.coords) != len(other.coords):
            raise ValueError("Vectors must have same lenght")
        new_coords = [a - b for a, b in zip(self.coords, other.coords)]
        return Vector(new_coords)

    def __mul__(self, other: "Vector") -> float:
        """
        Multiply vectors and return a number
        """
        if not isinstance(other, Vector):
            return NotImplemented
        if len(self.coords) != len(other.coords):
            raise ValueError("Vectors must have same lenght")
        return sum(a * b for a, b in zip(self.coords, other.coords))

    def __lt__(self, other: "Vector") -> bool:
        """
        Compare vectors by length less than
        """
        if not isinstance(other, Vector):
            return NotImplemented
        return self.length() < other.length()

    def __eq__(self, other: object) -> bool:
        """
        Compare vectors by length
        """
        if not isinstance(other, Vector):
            return NotImplemented
        return self.length() == other.length()

    def __repr__(self) -> str:
        """
        Return a string representation of the vector
        """
        return f"Vector({self.coords})"


if __name__ == "__main__":

    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])

    v3 = v1 + v2
    v4 = v2 - v1
    v5 = v1 * v2

    print(v3)
    print(v4)
    print(v5)

    print(v1.length())
    print(v1 < v2)
    print(v1 > v2)

    print(v1 == Vector([1, 2, 3]))

    print(v1 == "qwe")
