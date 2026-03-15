from EventExceptions import GameEventException
from GameEvents import event_details


def game_action(event_type: str) -> None:
    """
    Triggers a game event and raises a GameEventException with event details
    """
    try:
        details = event_details.get(event_type, "No info available")
        raise GameEventException(event_type, details)

    except GameEventException as ev:
        print(ev)


if __name__ == "__main__":

    events_to_catch = [
        "death",
        "levelUp",
        "itemFound",
        "questComplete",
        "unexpectedEvent",
        "i dont know what is going on",
    ]

    for event in events_to_catch:
        game_action(event)
