events = []


def daily_calendar():
    """Implement calendar event management using closures"""

    def add_event(event: str) -> None:
        """Add a new event"""
        events.append(event)

    def show_events():
        if not events:
            print("There is no upcoming events")
        else:
            print("Upcoming events:")
            for event in events:
                print(event)

    def remove_event(event: str) -> None:
        """Remove an event"""
        if event in events:
            events.remove(event)

    return add_event, show_events, remove_event


if __name__ == "__main__":
    add_event, show_events, remove_event = daily_calendar()
    add_event("Gym at 8:00")
    add_event("Coffe time at 10:00")
    add_event("Meeting at 11:00")
    add_event("Meeting at 14:00")

    show_events()

    remove_event("Meeting at 11:00")

    show_events()
