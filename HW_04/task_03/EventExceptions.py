class GameEventException(Exception):
    """
    Custom exception raised when a specific game event occurs
    """
    def __init__(self, event_type: str, details=None) -> None:
        self.event_type = event_type
        self.details = details
        super().__init__(f"Event '{event_type}' occurred. Info: {details}")
