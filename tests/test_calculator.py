# test_calculator.py

import pytest
from calculator_mod.calculator import Calculator

class TestCalculator:
    """
    Test class for the Calculator class
    """

    def test_operations(self, testdata):
        """
        Test operations of the Calculator class
        """
        for idx, (a, b, operation, expected) in enumerate(testdata):
            calculator = Calculator()
            if operation == "divide":
                if b == 0:
                    with pytest.raises(ValueError):
                        getattr(calculator, operation)(a, b)
                else:
                    result = getattr(calculator, operation)(a, b)
                    assert result == expected
            else:
                result = getattr(calculator, operation)(a, b)
                assert result == expected
