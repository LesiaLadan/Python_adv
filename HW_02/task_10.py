def create_product(name: str, price: int | float, amount: int):
    """Creates a product and returns a function to change its price"""
    item = {"name": name, "price": price, "amount": amount}

    def chage_price(new_price: int | float) -> None:
        """Set the newe product's price"""
        item["price"] = new_price

    return chage_price, item


if __name__ == "__main__":

    chage_price_funk, product = create_product("TV", 800, 2)
    print(product)
    chage_price_funk(900)
    print(product)
