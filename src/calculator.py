import math
import decimal


def sum(a, b):
    return a + b


def substrat(a, b):
    return a - b


def product(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return math.nan
    return a / b
