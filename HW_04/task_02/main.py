from pathlib import Path


def file_calculate_average(file_path: str) -> None:
    """Calculate average from numbers in file"""
    file = Path(file_path).name

    try:
        with open(file_path, "r") as my_file:
            lines = my_file.readlines()
            if not lines:
                print("File is empty")
                return

            numbers = []
            for line in lines:
                line = line.strip()
                if line:
                    try:
                        numbers.append(float(line))
                    except ValueError:
                        raise ValueError(f"Incorrect data in line: '{line}'")
            if len(numbers) == 1:
                print(f"Avarage for one number: {numbers[0]}")
            else:
                avarage = sum(numbers) / len(numbers)
                print(f"Avarage: {avarage}")

    except FileNotFoundError:
        print(f"'{file}' not found")
    except ValueError as err:
        print(err)


if __name__ == "__main__":
    filename = "HW_04/task_02/one_line.txt"
    file_calculate_average(filename)

    filename = "HW_04/task_02/bad_data.txt"
    file_calculate_average(filename)

    filename = "HW_04/task_02/empty.txt"
    file_calculate_average(filename)

    filename = "HW_04/task_02/numbers.txt"
    file_calculate_average(filename)

    filename = "HW_04/task_02/numbers.tt"
    file_calculate_average(filename)
