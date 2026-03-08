from typing import Literal


def create_calculator(oper: Literal["+", "-", "*", "/"]):
    """Simle calculator function for two numbers
    using a specified operator"""

    if oper not in {"+", "-", "*", "/"}:
        raise ValueError("Invalid operator")

    def calculate(a: float, b: float) -> float:
        """Perform the calculation with the
        perator specified in the outer function"""
        if oper == "+":
            return a + b
        if oper == "-":
            return a - b
        if oper == "*":
            return a * b
        if oper == "/":
            if b == 0:
                raise ValueError("Division by zero")
            return a / b

    return calculate


if __name__ == "__main__":

    add = create_calculator("+")
    sub = create_calculator("-")
    mul = create_calculator("*")
    div = create_calculator("/")

    print(add(10, 5))
    print(sub(10, 5))
    print(mul(10, 5))
    print(div(10, 5))

    try:
        print(create_calculator("/")(10, 0))
    except ValueError as error:
        print(error)

    try:
        print(create_calculator("//"))
    except ValueError as error:
        print(error)
