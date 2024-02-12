"""
Module containing tests for the Calculator class
"""

import pytest
from calculator_mod.calculator import Calculator
from calculator_mod import calculations

class TestCalculator:
    """
    Test class for the Calculator class
    """
    def setup_method(self):
        """
        Reset calculator history before each test
        """
        calculations.calculation_history.clear()

    @pytest.mark.parametrize("input_data, expected_result, expected_history", [
        ((2, 3, "add"), 5, ['2 + 3 = 5']),
        ((5, 3, "subtract"), 2, ['5 - 3 = 2']),
        ((2, 3, "multiply"), 6, ['2 * 3 = 6']),
        ((6, 3, "divide"), 2.0, ['6 / 3 = 2.0']),
        ((6, 0, "divide"), None, []),
        ((None, None, "get_history"), None, ['2 + 3 = 5', '5 - 3 = 2', '2 * 3 = 6', '6 / 3 = 2.0'])
    ])
    def test_operations(self, input_data, expected_result, expected_history):
        """
        Test operations of the Calculator class
        """
        calculator = Calculator()
        if input_data[2] == "divide":
            x, y, operation = input_data
            if y == 0:
                with pytest.raises(ValueError):
                    getattr(calculator, operation)(x, y)
            else:
                result = getattr(calculator, operation)(x, y)
                assert result == expected_result
                assert calculations.get_history() == expected_history
        elif input_data[2] == "get_history":
            calculator.add(2, 3)
            calculator.subtract(5, 3)
            calculator.multiply(2, 3)
            calculator.divide(6, 3)
            assert getattr(calculator, input_data[2])() == expected_history
        else:
            x, y, operation = input_data
            result = getattr(calculator, operation)(x, y)
            assert result == expected_result
            assert calculations.get_history() == expected_history
