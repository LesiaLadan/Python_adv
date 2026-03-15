from fundsException import InsufficientFundsException
from personBalance import person_balances


def transaction(person_balances: dict, transaction_sum: float, currency: str) -> dict:
    """
    Processes a transaction for a given currency and updates the balance
    """
    try:
        current_balance = person_balances.get(currency, 0.0)

        if current_balance < transaction_sum:
            raise InsufficientFundsException(transaction_sum, current_balance, currency)
        else:
            person_balances[currency] = current_balance - transaction_sum

            print(f"You have successfully transferred {currency}{transaction_sum:.2f}. "
                  f"Current balance: {currency}{person_balances[currency]:.2f}")

    except InsufficientFundsException as err:
        print(err)

    return person_balances


if __name__ == "__main__":

    transactions = [
        (20.889, "$"),
        (1.55, "$"),
        (5, "$"),
        (88, "$"),
        (50, "€"),
        (500, "₴"),
        (712, "₴")
    ]

    for amount, currency in transactions:
        transaction(person_balances, amount, currency)
