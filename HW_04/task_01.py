import math


class CalculatorException(Exception):
    """Base exception for calculator errors"""
    def __init__(self, message: str):
        super().__init__(message)


class UnknownOperationError(CalculatorException):
    """Exception for unknown operations"""
    def __init__(self, operation: str) -> None:
        super().__init__(f"Unknown operator: {operation}")


class CalcOverflowError(CalculatorException):
    """Exception for overflow"""
    def __init__(self, message: str) -> None:
        super().__init__(message)


def calculator(a: str, operation: str, b: str) -> None:
    try:
        first = float(a)
        second = float(b)
        result = None

        if operation == "+":
            result = first + second
        elif operation == "-":
            result = first - second
        elif operation == "*":
            result = first * second
        elif operation == "/":
            if second == 0:
                raise ZeroDivisionError("Division by zero isnt allowed")
            result = first / second
        else:
            raise UnknownOperationError(operation)

        if math.isinf(result):
            raise CalcOverflowError("Result is too large")

        print(f"Result: {result}")

    except ValueError as err:
        print(f"Value error: {err}")

    except ZeroDivisionError as err:
        print(f"Math error: {err}")

    except UnknownOperationError as err:
        print(f"Operation error: {err}")

    except CalcOverflowError as err:
        print(f"Overflow error: {err}")

    finally:
        print("\nCalculation finished")


if __name__ == "__main__":
    a = input("Enter first number: \n")
    operation = input("\nEnter operation (+, -, *, /): \n")
    b = input("\nEnter second namber: \n")
    calculator(a, operation, b)
