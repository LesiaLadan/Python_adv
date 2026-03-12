from decimal import Decimal


class Price:
    """Represents a monetary value rounded to two decimal places"""

    __slots__ = ("_amount",)

    def __init__(self, amount: Decimal | float | int | str) -> None:
        """Initialize a price value"""
        self._amount = self.round(Decimal(amount))

    @staticmethod
    def round(value: Decimal) -> Decimal:
        """Round a Decimal value to two digits using rounding"""
        return value.quantize(Decimal("0.01"))

    @property
    def amount(self) -> Decimal:
        """Return the underlying Decimal value"""
        return self._amount

    def __add__(self, other: "Price") -> "Price":
        """Return the sum of two Price objects"""
        if not isinstance(other, Price):
            return NotImplemented
        return Price(self._amount + other._amount)

    def __sub__(self, other: "Price") -> "Price":
        """Return the difference between two Price objects"""
        if not isinstance(other, Price):
            return NotImplemented
        return Price(self._amount - other._amount)

    def __eq__(self, other: object) -> bool:
        """Check equality between two Price values"""
        if not isinstance(other, Price):
            return False
        return self._amount == other._amount

    def __lt__(self, other: "Price") -> bool:
        """Return True if this price is less than another"""
        return self._amount < other._amount

    def __le__(self, other: "Price") -> bool:
        """Return True if this price is less or equal to another"""
        return self._amount <= other._amount

    def __repr__(self) -> str:
        """Return representation of the Price"""
        return f"Price({str(self._amount)})"


if __name__ == "__main__":

    p1 = Price("10.12334")
    p2 = Price(5.876)
    print("p1:", p1)
    print("p2:", p2)

    p3 = p1 + p2
    print("p1 + p2 =", p3)

    p4 = p1 - p2
    print("p1 - p2 =", p4)

    print("p1 == p2?", p1 == p2)
    print("p1 > p2?", p1 > p2)
    print("p1 < p2?", p1 < p2)
    print("p1 <= p2?", p1 <= p2)

    print("p3.amount =", p3.amount)
