from resousesException import InsufficientResourcesException
from playerResources import player_resources


def action(resource: str, required_amount: int) -> None:
    """Perform an action that needed specified resource"""
    try:
        current_amount = player_resources.get(resource, 0)
        if current_amount < required_amount:
            raise InsufficientResourcesException(
                resource,
                required_amount,
                current_amount
                )
        else:
            player_resources[resource] = current_amount - required_amount
            print(
                f"Action performed! Spent {required_amount} {resource}. "
                f"Remaining: {player_resources[resource]}"
            )

    except InsufficientResourcesException as warn:
        print(warn)


if __name__ == "__main__":

    actions_to_try = [
        ("gold", 40),
        ("mana", 50),
        ("stamina", 5),
        ("gold", 20),
        ("steel", 10)
    ]

    for resource, amount in actions_to_try:
        action(resource, amount)
