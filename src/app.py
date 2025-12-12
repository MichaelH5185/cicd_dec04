import math as m 

def add(a,b):
    return a+b

def multiply(a,b):
    return a*b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot Divide by Zero")
    return a/b

def sub(a,b):
    return a-b

def log(a, b):
    if a <= 0:
        raise ValueError("Log undefined for non-positive values")
    return m.log(a, b)

def square(a):
    return a*a

def sin(a):
    return m.sin(a)

def cos(a):
    return m.cos(a)

def square_root(a):
    if a < 0:
        raise ValueError("Cannot Square Root a Negative Number")
    return m.sqrt(a)

def percentage(a, b):
    return (a*b)/100