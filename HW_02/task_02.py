subscribers = []


def subscribe(name: str):
    """Add subscriber's name in the global 'subscribers' list"""

    subscribers.append(name)

    def confirm_subscription():
        """Return text about successful subscription"""

        print(f"Subscription confirmed for {name}")

    confirm_subscription()


def unsubscribe(name: str) -> str:
    """Remove specified subscriber from the global 'subscribers' list
    And returns a message about either the unsubscription was successful
    or the subscriber was not found"""

    if name in subscribers:
        subscribers.remove(name)
        return f"{name} has been successfully unsubscribed"
    return f"{name} was not found among subscribers"


if __name__ == "__main__":

    subscribe("Anna")
    subscribe("Ivan")
    subscribe("Olha")

    print("Current subscribers: ", subscribers)

    print(unsubscribe("Ivan"))
    print(unsubscribe("Petro"))

    print("Current subscribers: ", subscribers)
