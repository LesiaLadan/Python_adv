class InsufficientResourcesException(Exception):
    """Exception raised when a player does not have enough resources
    to perform an action"""

    def __init__(
        self, required_resource: str, required_amount: int, current_amount: int
    ) -> None:
        self.required_resource = required_resource
        self.required_amount = required_amount
        self.current_amount = current_amount
        super().__init__(
            f"Insufficient {self.required_resource}. "
            f"You have {self.current_amount}, "
            f"but {self.required_amount} are required"
        )
