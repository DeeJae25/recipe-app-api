"""
Calculator functions
"""


def add(x, y):
    return x+y


def subtract(x, y):
    res = x - y
    if res < 0:
        return -1 * res
    return res
