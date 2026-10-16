# from src.calculator import *

# def test_fun1():
#     assert fun1(2,3) == 5

# def test_fun2():
#     assert fun2(2,3) == -1

# def test_fun3():
#     assert fun3(2,3) == 6

# def test_fun4():
#     assert fun4(2,3) == 10

# def test_fun5():
#     assert fun4(11,3) == 2

import pytest
from src import calculator

def test_fun1():
    assert calculator.fun1(2, 3) == 5
    assert calculator.fun1(5,0) == 5
    assert calculator.fun1 (-1, 1) == 0
    assert calculator.fun1 (-1, -1) == -2


def test_fun2():
    assert calculator.fun2(2, 3) == -1
    assert calculator.fun2(5,0) == 5
    assert calculator.fun2 (-1, 1) == -2
    assert calculator.fun2 (-1, -1) == 0

def test_fun3():
    assert calculator.fun3(2, 3) == 6
    assert calculator.fun3(5,0) == 0
    assert calculator.fun3 (-1, 1) == -1
    
    assert calculator.fun3 (-1, -1) == 1

def test_fun4():
    assert calculator.fun4(2, 3, 5) == 10
    assert calculator.fun4(5,0, -1) == 4
    assert calculator.fun4 (-1, -1, -1) == -3
    
    assert calculator.fun4 (-1, -1, 100) == 98

def test_fun5():
    # assert fun4(11,3) == 2
    assert calculator.fun5 (10, 5) == 0

def test_divide_numbers():
    # assert fun4(11,3) == 2
    assert calculator.divide_numbers(10, 5) == 2
    assert calculator.divide_numbers(15, 3) == 5
    assert calculator.divide_numbers(18, 6) == 3

def test_fun5():
    # assert fun4(11,3) == 2
    assert calculator.power_numbers(2, 3) == 8
    assert calculator.power_numbers(5, 2) == 25
    assert calculator.power_numbers(3, 3) == 27


