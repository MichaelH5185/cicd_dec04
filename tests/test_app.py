import pytest 
from src.app import add, multiply, divide, sub

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    
def test_sub():
    assert sub(10, 5) == 5

def test_multi():
    assert multiply(5,5) == 25

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)