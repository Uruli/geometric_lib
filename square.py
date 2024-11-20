def area(a):
    if a < 0:
        raise AssertionError("Can't")
    return a * a


def perimeter(a):
    if a < 0:
        raise AssertionError("Can't")
    return 4 * a
