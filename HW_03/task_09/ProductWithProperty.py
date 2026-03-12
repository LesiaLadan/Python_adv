class ProductWithProperty:
    """
    Product using properties for price
    """
    def __init__(self, name, price) -> None:
        """
        Initialize a Product instance
        """
        self.name = name
        self._price = 0.00
        self.price = price

    @property
    def price(self) -> float:
        """
        Get the current price of the product
        """
        return self._price

    @price.setter
    def price(self, value) -> None:
        """
        Set the current price of the product
        """
        if value < 0:
            raise ValueError("Price cant be negative")
        self._price = value
