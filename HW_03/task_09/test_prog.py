from ProductWithGetSet import ProductWithGetSet
from ProductWithProperty import ProductWithProperty
from ProductWithDescriptor import ProductWithDescriptor


def test_get_set_implementation():

    p1 = ProductWithGetSet("Laptop", 8890.00)
    print(f"Initial price: {p1.get_price()}")

    p1.set_price(1287.00)
    print(f"Updated price: {p1.get_price()}")

    try:
        p1.set_price(-50.77)
    except ValueError as err:
        print(err)
    print()


def test_property_implementation():
    p2 = ProductWithProperty("Smartphone", 590.10)
    print(f"Initial price: {p2.price}")

    p2.price = 978.03
    print(f"Updated price: {p2.price}")

    try:
        p2.price = -190.36
    except ValueError as err:
        print(err)
    print()


def test_descriptor_implementation():
    p3 = ProductWithDescriptor("Tablet", 38.90)
    print(f"Initial price: {p3.price}")

    p3.price = 48.06
    print(f"Updated price: {p3.price}")

    try:
        p3.price = -20.97
    except ValueError as err:
        print(err)
    print()


if __name__ == "__main__":
    test_get_set_implementation()
    test_property_implementation()
    test_descriptor_implementation()
