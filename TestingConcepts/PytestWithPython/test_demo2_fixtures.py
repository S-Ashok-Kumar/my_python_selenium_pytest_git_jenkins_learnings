"""
Command to run:
python -m pytest PytestWithPython/test_demo2_fixtures.py -s -v

1. Fixtures (Ex: Common utilities)
        * @pytest.fixture
        * Is a reusable function
        * It also returns the value
"""

import pytest

# @pytest.fixture - marks setup() as a fixture — a reusable function that can run before (and optionally after) each test.
# When you include setup as a parameter in a test function (Ex: test_one(setup)), Pytest automatically calls it first.
@pytest.fixture
def setup():
    print("Launch the browser")

# pass setup as parameter into test_one(), else the setup() can not execute before every method
def test_one(setup):
    print("this is my test one")

def test_two(setup):
    print("this is my test two")

def test_three(setup):
    print("this is my test three")


"""
Output:
collected 3 items                                                                                                                                    

PytestWithPython/test_demo2_fixtures.py::test_one Launch the browser
this is my test one
PASSED                                                                                                                                               
PytestWithPython/test_demo2_fixtures.py::test_two Launch the browser
this is my test two
PASSED                                                                                                                                               
PytestWithPython/test_demo2_fixtures.py::test_three Launch the browser
this is my test three
PASSED                                                                                                                                               

"""
