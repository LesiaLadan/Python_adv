import random

default_time = 60


def training_session(rounds: int) -> None:
    """
    Simulate a training session
    Each round can be adjusted using an internal nested function
    """

    time_per_round = default_time

    def adjust_time(time_change: int) -> None:
        """Adjust the time for the current round"""
        nonlocal time_per_round
        time_per_round += time_change

    for round_number in range(1, rounds + 1):

        if round_number > 1:
            random_change = random.randint(-10, 10)
            adjust_time(random_change)

        hours = time_per_round // 60
        minutes = time_per_round % 60

        print(f"Round {round_number}: {hours} h {minutes} min")


if __name__ == "__main__":
    training_session(14)
