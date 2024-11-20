from math import sqrt


def area(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise AssertionError("Can't")
    x = (a + b + c) / 2
    return sqrt(x * (x - a) * (x - b) * (x - c))


def perimeter(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise AssertionError("Can't")
    return a + b + c
