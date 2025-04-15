#https://github.com/JuanCavallin/Lab10-JC-KG
#Partner 1: Juan Cavallin
#Partner 2: Kieran Galveston
import math

def square_root(a):
    if a < 0:
        raise ValueError()
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.sqrt((a ** 2 + b ** 2))

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if a == 0:
        raise ZeroDivisionError()
    return b / a
def logarithm(a, b):
    if a <= 0 or b <= 1:
        raise ValueError()
    return math.log(b, a)
def exponent(a, b):
    return a ** b

