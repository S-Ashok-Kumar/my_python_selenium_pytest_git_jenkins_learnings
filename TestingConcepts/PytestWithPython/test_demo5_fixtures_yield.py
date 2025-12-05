"""
Command to run:
python -m pytest PytestWithPython/test_demo5_fixtures_yield.py -s -v

Close the browser:

Yield:
    Once a fixture uses yield, the return value is ignored.
A fixture with yield has two parts:
Before the test → Setup code (runs before the test)
After the test → Teardown code (runs after the test)
"""
import pytest

@pytest.fixture
def setup():
    print("Launch the browser")
    yield
    print("Close browser")

def test_one(setup):
    print("this is my test one")

def test_two(setup):
    print("this is my test two")

def test_three(setup):
    print("this is my test three")


"""
Output:

collected 3 items                                                                                                                                   

PytestWithPython/test_demo5_fixtures_yield.py::test_one Launch the browser
this is my test one
PASSEDClose browser

PytestWithPython/test_demo5_fixtures_yield.py::test_two Launch the browser
this is my test two
PASSEDClose browser

PytestWithPython/test_demo5_fixtures_yield.py::test_three Launch the browser
this is my test three
PASSEDClose browser
"""