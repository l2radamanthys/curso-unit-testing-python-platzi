import math
import decimal


def sum(a, b):
    """
    >>> sum(5, 7)
    12

    >>> sum(4, -4)
    0
    """
    return a + b


def substrat(a, b):
    return a - b


def product(a, b):
    return a * b


def divide(a, b):
    """
    >>> divide(10, 0)
    Traceback (most recent call last):
    ValueError: No esta permitida la division por 0
    """
    if b == 0:
        raise ValueError("No esta permitida la division por 0")
    return a / b
