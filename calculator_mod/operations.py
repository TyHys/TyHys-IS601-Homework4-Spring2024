"""
Defines the basic arithmetic methods/functions
"""
@staticmethod
def add(x, y):
    """Returns the result of two added numbers"""
    return x + y

@staticmethod
def subtract(x, y):
    """Returns the result of two subtracted numbers"""
    return x - y

@staticmethod
def multiply(x, y):
    """Returns the result of two multiplied numbers"""
    return x * y

@staticmethod
def divide(x, y):
    """Returns the result of two divided numbers"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y
