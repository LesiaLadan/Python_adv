class Fraction:
    """Represents a fraction and supports basic arithmetic operations"""

    def __init__(self, num: int, den: int) -> None:
        """Initialize fraction with numerator and denominator where:\n
        - param num - numerator\n
        - param den - denominator
        """
        if den == 0:
            raise ValueError("Denominator cannot be zero")
        self.num: int = num
        self.den: int = den

    def __add__(self, other: "Fraction") -> "Fraction":
        """Add two fractions"""
        if not isinstance(other, Fraction):
            return NotImplemented
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        return Fraction(num, den)

    def __sub__(self, other: "Fraction") -> "Fraction":
        """Subtract two fractions"""
        if not isinstance(other, Fraction):
            return NotImplemented
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        return Fraction(num, den)

    def __mul__(self, other: "Fraction") -> "Fraction":
        """Multiply two fractions."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other: "Fraction") -> "Fraction":
        """Divide two fractions."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(self.num * other.den, self.den * other.num)

    def __repr__(self) -> str:
        """Return fraction in 'numerator/denominator' format."""
        return f"{self.num}/{self.den}"


if __name__ == "__main__":
    try:
        f0 = Fraction(2, 0)
    except ValueError as err:
        print(err)

    f1 = Fraction(2, 3)
    f2 = Fraction(3, 6)
    f3 = f1 + f2

    print(f1)
    print(f2)
    print(f3)
    print((f1 + f2))
    print((f1 * f2))
    print((f1 - f2))
    print((f1 / f2))
