"""
Command to run:
python -m pytest PytestWithPython/mypackdemo6/test_logins.py -s -v

This file access the fixtures from "conftest.py"
You can run this file individually by using above "above command".
"""

import pytest

def test_LoginByEmail(setup):
    print("Login by email test case")
    assert True==True

def test_LoginByFb(setup):
    print("Login by Facebook test case")
    assert True==True

def test_LoginByPhone(setup):
    print("Login by Phone test case")
    assert True==True


"""
Output:
collected 3 items                                                                                                                                   

PytestWithPython/mypackdemo6/test_logins.py::test_LoginByEmail Setup Environment
Login by email test case
PASSEDTearDown.....

PytestWithPython/mypackdemo6/test_logins.py::test_LoginByFb Setup Environment
Login by Facebook test case
PASSEDTearDown.....

PytestWithPython/mypackdemo6/test_logins.py::test_LoginByPhone Setup Environment
Login by Phone test case
PASSEDTearDown.....
"""