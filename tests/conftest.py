# conftest.py
import pytest
from decimal import Decimal
from faker import Faker
from calculator_mod.operations import add, subtract, multiply, divide

fake = Faker()

@pytest.fixture(scope="session")
def testdata(request):
    # Define operation mappings for both Calculator and Calculation tests
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    num_records = request.config.getoption("--num_records")
    # Generate test data
    test_data = []
    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]
        
        # Ensure b is not zero for divide operation to prevent division by zero in expected calculation
        if operation_func == divide:
            b = Decimal('1') if b == Decimal('0') else b
        
        try:
            if operation_func == divide and b == Decimal('0'):
                expected = "ZeroDivisionError"
            else:
                expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"
        
        test_data.append((a, b, operation_name, expected))
    
    return test_data

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")
