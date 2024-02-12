"""
Methods used to define and retrieve the history of calculations
"""

calculation_history = []

def add_to_history(equation):
    """Adds a equation in the form of a string to the calculation_history list"""
    calculation_history.append(equation)

def get_history():
    """Retrieves the calculation_history list and returns it"""
    return calculation_history
