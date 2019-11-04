from file2 import Calculator
import pytest

@pytest.mark.add #now we can call this function only by running (pytest -m add)
def test_add():

    calculator = Calculator()

    result = calculator.add(2,3)

    assert result == 5

@pytest.mark.subtract
def test_subtract():

    calculator = Calculator()

    result = calculator.subtract(9,3)

    assert result == 6

 
@pytest.mark.multiply
def test_multiply():

    calculator = Calculator()

    result = calculator.multiply(2,3)

    assert result == 6


