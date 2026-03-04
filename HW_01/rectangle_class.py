class Rectangle:
    """
    A class representing a rectangle with attr:
        width
        height
    """

    def __init__(self, width: float, height: float):
        """
        Initialize a rectangle with a given width and height
        """
        self.width = width
        self.height = height

    def area(self) -> float:
        """
        Calculate the area of the rectangle
        """
        area = self.width * self.height

        return area

    def perimeter(self) -> float:
        """
        Calculate the perimeter of the rectangle
        """
        return (self.width + self.height) * 2

    def is_square(self) -> bool:
        """
        Check if the rectangle is a square
        """
        return self.width == self.height

    def resize(self, new_width: float, new_height: float):
        """
        Resize the rectangle to a new height and width
        """
        self.width = new_width
        self.height = new_height

    def __str__(self):
        return f"Rectangle with width {self.width} and height {self.height}"


if __name__ == "__main__":

    rectangle_1 = Rectangle(2.9, 8)
    rectangle_1.resize(5, 5)

    print(rectangle_1)
    print("Area:", rectangle_1.area())
    print("Perimeter:", rectangle_1.perimeter())
    print("Is square?", rectangle_1.is_square())

    rectangle_1.resize(5, 5)

    print("After resizing:", rectangle_1)
    print("New area:", rectangle_1.area())
    print("New perimeter:", rectangle_1.perimeter())
    print("Is square now?", rectangle_1.is_square())
