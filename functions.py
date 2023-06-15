"""This file contains a basic intro fo functions"""


def add():
    """Code to add two numbers"""
    return 1 + 1


print(add())


def add1(val_1, val_2):
    """Takes two values and adds them"""
    return val_1 + val_2


print(add1(1, 1))


def add2(*val):
    """Takes any number of values and adds them"""
    tot = 0
    for i in val:
        tot = tot + i
    return tot


print(add2(1, 1, 1))
