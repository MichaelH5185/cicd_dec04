import sys
from pathlib import Path
root = Path(__file__).resolve().parents[1]

from app import multiply, add, divide, sub

def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(5, 6) != 10