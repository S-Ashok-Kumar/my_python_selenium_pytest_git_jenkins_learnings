"""
Lesson-1: How to create a module? How to create test cases? How to create class?
In pytest, we don’t need to manually call functions or create objects for classes to run tests.
Pytest automatically discovers and executes them based on naming conventions.

Command to run from CMD:
    python -m pytest PytestWithPython/test_demo1.py     -> This command just show the test case is pass/fail | runs all test cases
Command to print the print statements in the output console: (-s means see all test cases and print statements in the console)
    python -m pytest PytestWithPython/test_demo1.py -s
Command to execute only specific test cases:
     python -m pytest PytestWithPython/test_demo1.py::test_one -s

USE BELOW COMMAND TO EXECUTE THIS MODULE:
Command to get extra detailed information in console: (-v means verbose mode)
     python -m pytest PytestWithPython/test_demo1.py -s -v
"""

# Preferred way
import pytest

def test_one():
    print("this is my test one")

def test_two():
    print("this is my test two")

def test_three():
    print("this is my test three")

"""
Output:
collected 3 items                                                                                                                                   

PytestWithPython/test_demo1.py::test_one this is my test one
PASSED
PytestWithPython/test_demo1.py::test_two this is my test two
PASSED
PytestWithPython/test_demo1.py::test_three this is my test three
PASSED

"""

"""
# Ignore this process in pytest.
# Example for creating a class and running test cases.

class TestClass:
    def test_one(self):
        print("this is my test one")

    def test_two(self):
        print("this is my test two")

    def test_three(self):
        print("this is my test three")
"""
"""
Output:
collected 3 items                                                                                                                                   

PytestWithPython/test_demo1.py::TestClass::test_one this is my test one
PASSED
PytestWithPython/test_demo1.py::TestClass::test_two this is my test two
PASSED
PytestWithPython/test_demo1.py::TestClass::test_three this is my test three
PASSED
"""