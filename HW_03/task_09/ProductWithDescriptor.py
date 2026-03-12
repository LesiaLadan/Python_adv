class PriceDescriptor:
    """Descriptor for the 'price' attribute """
    def __init__(self) -> None:
        """
        Initialize the PriceDescriptor
        """
        self._values = {}

    def __get__(self, instance, owner=None):
        """
        Get the current price of the product instance
        """
        if instance is None:
            return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value) -> None:
        """
        Set the current price of the product instance
        """
        if value < 0:
            raise ValueError("Price cant be negative")
        self._values[instance] = value


class ProductWithDescriptor:
    """
    Product using description for price
    """
    price = PriceDescriptor()

    def __init__(self, name, price) -> None:
        """
        Initialize a Product instance
        """
        self.name = name
        self.price = price
