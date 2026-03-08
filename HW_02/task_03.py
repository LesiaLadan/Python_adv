discount = 0.1


def create_order(price: float) -> None:
    """Create an order and apply available discounts"""

    final_price = price * (1 - discount)
    print(f"Final price after common discount: {final_price}")

    def apply_additional_discount() -> None:
        """Apply an additional VIP discount to the final price"""
        nonlocal final_price
        vip_discount = 0.05
        final_price *= 1 - vip_discount

    apply_additional_discount()
    print(f"Final price after VIP discount: {final_price}")


if __name__ == "__main__":
    create_order(1000)
