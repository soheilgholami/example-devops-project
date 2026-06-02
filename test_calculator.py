import pytest
from calculator import add, subtract, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 2) == 3

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    # We expect this to raise an error — that's the correct behavior.
    with pytest.raises(ValueError):
        divide(1, 0)