from file2 import Calculator , CalculatorError
import pytest

@pytest.mark.add #now we can call this function only by running (pytest -m add)
def test_add():

    calculator = Calculator()

    result = calculator.add(2,3)

    assert result == 5



def test_add_weird_stuff(): #now leave this function , like what we do in unitest ... ExpectedFailure

    calculator = Calculator()

    with pytest.raises(CalculatorError):
        result = calculator.add("two",3)



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


@pytest.mark.divide
def test_divide():

    calculator = Calculator()

    result = calculator.divide(10,2)

    assert result == 5



