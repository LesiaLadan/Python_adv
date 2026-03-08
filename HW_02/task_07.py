total_expense = 0.0


def add_expense(summ: float) -> None:
    """Adds the given amount to the global total_expense"""
    global total_expense
    total_expense += summ


def get_expense() -> float:
    """Returns the current total of all expenses"""
    return total_expense


if __name__ == "__main__":
    while True:
        print(
            "\nEnter 1 for adding expense\nEnter 2 to show your total expense\nEnter 3 for exit\n"
        )
        choice = input("Choose option: ")

        if choice == "1":
            try:
                add_expense(float(input("Enter expense: ")))
            except ValueError:
                print("Entered simbols are not numbers!")
        elif choice == "2":
            print(f"Total expense: {get_expense()}")
        elif choice == "3":
            break
        else:
            print("Invalid option. Enter 1, 2 or 3")
