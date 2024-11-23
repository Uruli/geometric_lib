import math


def area(r):
    if r < 0:
        raise AssertionError("Can't")
    return math.pi * r * r


def perimeter(r):
    if r < 0:
        raise AssertionError("Can't")
    return 2 * math.pi * r
