"""
Command to Run:
python -m pytest PytestWithPython/test_demo7_skipping.py -s -v

To beautify the code: CTRL+A -> CTRL+ALT+L
Skipping the testcases: @pytest.mark.skip
"""

import pytest


def test_loginbyemail():
    print("this is login by email test")
    assert 1 == 1

@pytest.mark.skip       # (We call it decorators) To skip the test case at run time.
def test_loginbyfb():
    print("this is login by facebook test")
    assert 1 == 1

@pytest.mark.skip
def test_loginbyphone():
    print("this is login by phone test")
    assert 1 == 1


def test_signupbyemail():
    print("this is signup by email test")
    assert 1 == 1

@pytest.mark.skip
def test_signupbyfb():
    print("this is signup by facebook test")
    assert 1 == 1

@pytest.mark.skip
def test_signupbyphone():
    print("this is signup by phone test")
    assert 1 == 1

"""
Output:
collected 6 items                                                                                                                                   

PytestWithPython/test_demo7_skipping.py::test_loginbyemail this is login by email test
PASSED
PytestWithPython/test_demo7_skipping.py::test_loginbyfb SKIPPED (unconditional skip)
PytestWithPython/test_demo7_skipping.py::test_loginbyphone SKIPPED (unconditional skip)
PytestWithPython/test_demo7_skipping.py::test_signupbyemail this is signup by email test
PASSED
PytestWithPython/test_demo7_skipping.py::test_signupbyfb SKIPPED (unconditional skip)
PytestWithPython/test_demo7_skipping.py::test_signupbyphone SKIPPED (unconditional skip)

=========================================================== 2 passed, 4 skipped in 0.11s
"""