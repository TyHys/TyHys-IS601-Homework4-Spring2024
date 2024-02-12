"""
Defines the calculator class, to be used for performing arithmetic
"""

from calculator_mod import calculations
from calculator_mod import operations

class Calculator:
    """
    Creates a Calculator class, which will pass arguments to the operations methods
    and will use the calculations import to add/retrieve history
    """
    def add(self, x, y):
        """Defines the path that a Calculator takes when adding two numbers"""
        result = operations.add(x, y)
        equat = f'{x} + {y} = {result}'
        self._update_history(equat)
        return result

    def subtract(self, x, y):
        """Defines the path that a Calculator takes when subtracting two numbers"""
        result = operations.subtract(x, y)
        equat = f'{x} - {y} = {result}'
        self._update_history(equat)
        return result

    def multiply(self, x, y):
        """Defines the path that a Calculator takes when multiplying two numbers"""
        result = operations.multiply(x, y)
        equat = f'{x} * {y} = {result}'
        self._update_history(equat)
        return result

    def divide(self, x, y):
        """Defines the path that a Calculator takes when Dividing two numbers"""
        result = operations.divide(x, y)
        equat = f'{x} / {y} = {result}'
        self._update_history(equat)
        return result

    def _update_history(self, equation):
        """Defines Calculators path to add to Calculator history"""
        calculations.add_to_history(equation)

    def get_history(self):
        """Defines the path that a Calculator takes when retrieving the history"""
        return calculations.get_history()
