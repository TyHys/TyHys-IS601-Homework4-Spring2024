"""
Entry point for the calculator application.
"""

import sys
from decimal import Decimal, InvalidOperation
from calculator_mod.calculator import Calculator

def main():
    """
    Main function for the calculator application.
    """
    if len(sys.argv) != 4:
        print("Usage: python main.py <number1> <number2> <operation>")
        sys.exit(1)

    _, a, b, operation = sys.argv
    calculator = Calculator()
    try:
        result = getattr(calculator, operation)(Decimal(a), Decimal(b))
        print(f"The result of {a} {operation} {b} is equal to {result}")
    except AttributeError:
        print(f"Unknown operation: {operation}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
