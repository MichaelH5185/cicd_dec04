import pytest 
from src.app import add, multiply, divide, sub, log, square, sin, cos, square_root, percentage

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
def test_log():
    with pytest.raises(ValueError):
        log(0, 10)
    assert log(10, 10) == 1

def test_square():
    assert square(2) == 4

def test_sin():
    assert sin(0) == 0
    
def test_cos():
    assert cos(0) == 1

def test_sqrt():
    with pytest.raises(ValueError):
        square_root(-1)
    assert square_root(144) == 12

def test_percentage():
    assert percentage(200, 10) == 20