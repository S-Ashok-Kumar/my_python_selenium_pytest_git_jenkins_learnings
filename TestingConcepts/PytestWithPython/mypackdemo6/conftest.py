"""
This file is common for the modules (test_logins.py, test_signups.py) in same package.
file name should be "conftest.py" (otherwise pytest didn't identify)
This file contains only fixtures (common utilities). Can be (reusable) accessible across all the modules.
You can directly run the complete package in one shot using below command
        ** python -m pytest PytestWithPython/mypackdemo6 -s -v **
                                        or
        ** Right click on "mypackdemo6" -> click "Run 'python test in mypackdemo6'" **
"""
import pytest

@pytest.fixture
def setup():
    print("Setup Environment")
    yield
    print("TearDown.....")


"""
Output if you run the complete package:

collected 6 items                                                                                                                                   

PytestWithPython/mypackdemo6/test_logins.py::test_LoginByEmail Setup Environment
Login by email test case
PASSEDTearDown.....

PytestWithPython/mypackdemo6/test_logins.py::test_LoginByFb Setup Environment
Login by Facebook test case
PASSEDTearDown.....

PytestWithPython/mypackdemo6/test_logins.py::test_LoginByPhone Setup Environment
Login by Phone test case
PASSEDTearDown.....

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