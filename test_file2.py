from file2 import Calculator
import pytest

@pytest.mark.add
def test_add():

    calculator = Calculator()

    result = calculator.add(2,3)

    assert result == 5


def test_subtract():

    calculator = Calculator()

    result = calculator.subtract(9,3)

    assert result == 6





