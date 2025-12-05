"""
Command to Run:
python -m pytest PytestWithPython/test_demo9_ordering.py -s -v

Pre-requisite: install pytest-order plugin
Command to install: pip install pytest-order

* @pytest.mark.order(Number)
* @pytest.mark.order(before/after="Test_Case_name")
* @pytest.mark.order("first/last")

Helps to maintain the order of execution of test functions.
In selenium, we will achieve this by priority notation (Java).
    Ex:
    import org.testng.annotations.Test;

    public class PriorityExample {

        @Test(priority = 1)
        public void openBrowser() {
            System.out.println("Open Browser");
        }

        @Test(priority = 2)
        public void login() {
            System.out.println("Login to application");
        }
"""

import pytest

# # Approach 1: Order tests by position
# # Even if you change the order the test functions will execute based on order number (1, 2, 3)

@pytest.mark.order(3)
def test_logout():
    print("This is logout")


@pytest.mark.order(1)
def test_login():
    print("This is login test")


@pytest.mark.order(2)
def test_add_item():
    print("This is add item test")

"""
Output:
collected 3 items                                                                                                                                   

PytestWithPython\test_demo9_ordering.py::test_login This is login test
PASSED
PytestWithPython\test_demo9_ordering.py::test_add_item This is add item test
PASSED
PytestWithPython\test_demo9_ordering.py::test_logout This is logout
PASSED

================================================================ 3 passed in 0.09
"""

# # Approach 2: Using before, after
# # Even if you change the order the test functions will execute based on order number (1, before, after)

# @pytest.mark.order(before="test_logout")
# def test_add_item():
#     print("This is add item test")
#
#
# @pytest.mark.order(1)
# def test_login():
#     print("This is login test")
#
#
# @pytest.mark.order(after="test_add_item")
# def test_logout():
#     print("This is logout")

"""
Output:
collected 3 items                                                                                                                                    

PytestWithPython\test_demo9_ordering.py::test_login This is login test
PASSED
PytestWithPython\test_demo9_ordering.py::test_add_item This is add item test
PASSED
PytestWithPython\test_demo9_ordering.py::test_logout This is logout
PASSED

================================================================ 3 passed in 0.11
"""


# # Approach 3: Using marker string (user defined)

# @pytest.mark.order("first")
# def test_login():
#     print("This is login test")
#
# @pytest.mark.order("last")
# def test_logout():
#     print("This is logout")
#
# @pytest.mark.order()
# def test_add_item():
#     print("This is add item test")

"""
Output:
collected 3 items                                                                                                                                   

PytestWithPython\test_demo9_ordering.py::test_login This is login test
PASSED
PytestWithPython\test_demo9_ordering.py::test_add_item This is add item test
PASSED
PytestWithPython\test_demo9_ordering.py::test_logout This is logout
PASSED

================================================================ 3 passed in 0.11s
"""