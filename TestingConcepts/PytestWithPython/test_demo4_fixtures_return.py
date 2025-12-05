"""
Command to run:
python -m pytest PytestWithPython/test_demo4_fixtures_return.py -s -v

1. Fixtures (Ex: Common utilities)
        * It also returns the value
        * Is a reusable function
"""

import pytest

@pytest.fixture
def setup():            # setup() is a fixture function.
    print("Launch the browser")
    return "Chrome"

# setup inside a test is a variable. It receives the Chrome from setup() fixture.
def test_one(setup):
    print("this is my test one")
    print("Browser is: ", setup)

# Here fixture setup is not provided as parameter inside test_two(). So, fixture setup doesn't execute.
def test_two():
    print("this is my test two")

# Here fixture setup is not provided as parameter inside test_three(). So, fixture setup doesn't execute.
def test_three():
    print("this is my test three")

"""
Output:
collected 3 items                                                                                                                                   

PytestWithPython/test_demo4_fixtures_return.py::test_one Launch the browser
this is my test one
Browser is:  Chrome
PASSED
PytestWithPython/test_demo4_fixtures_return.py::test_two this is my test two
PASSED
PytestWithPython/test_demo4_fixtures_return.py::test_three this is my test three
PASSED

"""