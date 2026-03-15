class InsufficientFundsException(Exception):
    """
    Exception raised when a transaction cannot be
    completed due to insufficient funds.
    """
    def __init__(self, required_amount: float, current_balance: float, currency: str) -> None:
        self.required_amount = required_amount
        self.current_balance = current_balance
        self.currency = currency
        super().__init__(f"Transaction declined: insufficient funds. "
                         f"Required amount: {self.currency}{required_amount:.2f}, "
                         f"current balance: {self.currency}{self.current_balance:.2f}.")