"""this file contains test cases for functions.py"""
from lesson1.functions import add, add1, add2


def test_add():
    """test the add funtion"""
    result = add()
    assert result == 2


def test_add1():
    """test the add1 funtion"""
    result = add1(1, 1)
    assert result == 2


def test_add2():
    """test the add2 funtion"""
    result = add2(1, 1, 1)
    assert result == 3
