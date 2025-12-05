"""
Command to run:
python -m pytest PytestWithPython/mypackdemo6/test_signups.py -s -v

This file access the fixtures from conftest.py
You can run this file individually by using above "above command".
"""

import pytest

def test_signupbyEmail(setup):
    print("This is signup by Email test")
    return True==True

def test_signupbyFb(setup):
    print("This is signup by Facebook test")
    return True==True

def test_signupbyPhone(setup):
    print("This is signup by Phone test")
    return True==True

"""
Output:
collected 3 items                                                                                                                                    

PytestWithPython/mypackdemo6/test_signups.py::test_signupbyEmail Setup Environment
This is signup by Email test
PASSEDTearDown.....

PytestWithPython/mypackdemo6/test_signups.py::test_signupbyFb Setup Environment
This is signup by Facebook test
PASSEDTearDown.....

PytestWithPython/mypackdemo6/test_signups.py::test_signupbyPhone Setup Environment
This is signup by Phone test
PASSEDTearDown.....

"""