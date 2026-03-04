import math


def calculate_circle_area(radius: float) -> float:
    """ This func culculates circle area"""
    return math.pi * radius ** 2


if __name__ == "__main__":

    while True:
        radius_input = input("Enter radius: \n")
        try:
            radius = float(radius_input)
            break
        except ValueError:
            print("Error: invalid number\n")
    area = calculate_circle_area(radius)

    print(f"The area of the circle with radius {radius} is {area:.2f}")
