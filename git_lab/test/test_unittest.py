import sys
import os
import unittest

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import calculator


class TestCalculator(unittest.TestCase):

    def test_fun1(self):
        self.assertEqual(calculator.fun1(2, 3), 5)
        self.assertEqual(calculator.fun1(5, 0), 5)
        
        self.assertEqual(calculator.fun1(-1, 1), 0)
        self.assertEqual(calculator.fun1(-1, -1), -2)

    def test_fun2(self):
        self.assertEqual(calculator.fun2(2, 3), -1)
        self.assertEqual(calculator.fun2(5, 0), 5)
        self.assertEqual(calculator.fun2(-1, 1), -2)
        self.assertEqual(calculator.fun2(-1, -1), 0)

    def test_fun3(self):
        self.assertEqual(calculator.fun3(2, 3), 6)
        self.assertEqual(calculator.fun3(5, 0), 0)
        self.assertEqual(calculator.fun3(-1, 1), -1)
        self.assertEqual(calculator.fun3(-1, -1), 1)

    def test_fun4(self):
        self.assertEqual(calculator.fun4(2, 3, 5), 10)
        self.assertEqual(calculator.fun4(5, 0, -1), 4)
        self.assertEqual(calculator.fun4(-1, -1, -1), -3)
        self.assertEqual(calculator.fun4(-1, -1, 100), 98)

    def test_fun5(self):
        self.assertEqual(calculator.fun5(2, 3), 2)
        self.assertEqual(calculator.fun5(15, 4), 3)
        self.assertEqual(calculator.fun5(20, 7), 6)
        self.assertEqual(calculator.fun5(30, 5), 0)

    def test_divide_numbers(self):
        self.assertEqual(calculator.divide_numbers(9, 3), 3)
        self.assertEqual(calculator.divide_numbers(15, 3), 5)
        self.assertEqual(calculator.divide_numbers(20, 4), 5)
        self.assertEqual(calculator.divide_numbers(30, 5), 6)

    def test_power_numbers(self):
        self.assertEqual(calculator.power_numbers(2, 1), 2)
        self.assertEqual(calculator.power_numbers(3, 2), 9)
        self.assertEqual(calculator.power_numbers(5, 3), 125)
        self.assertEqual(calculator.power_numbers(7, 2), 49)

if __name__ == '__main__':
    unittest.main()


# import os
# import sys
# import unittest

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# from calculator import *

# class TestCalculator(unittest.TestCase):

#     def test_fun1(self):
#         self.assertEqual(fun1(2,3), 5)

#     def test_fun2(self):
#         self.assertEqual(fun2(2,3), -1)

#     def test_fun3(self):
#         self.assertEqual(fun3(2,3), 6)

#     def test_fun4(self):
#         self.assertEqual(fun4(2,3), 10)

#     def test_fun5(self):
#         self.assertEqual(fun4(11,3), 2)

# if __name__ == '__main__':
#     unittest.main()