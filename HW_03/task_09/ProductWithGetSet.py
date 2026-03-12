class ProductWithGetSet:
    """
    Product using getter/setter for price
    """

    def __init__(self, name: str, price: float) -> None:
        """
        Initialize a Product instance
        """
        self.name = name
        self._price = 0.00
        self.set_price(price)

    def get_price(self) -> float:
        """
        Get the current price of the product
        """
        return self._price

    def set_price(self, value: float) -> None:
        """
        Set a new price for the product
        """
        if value < 0:
            raise ValueError("Price cant be negative")
        self._price = value
