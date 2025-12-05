"""
Command to Run:
python -m pytest PytestWithPython/test_demo8_grouping.py -s -v

Grouping the testcases - sanity, regression....
* @pytest.mark.[User_defined_name]
        Ex: @pytest.mark.Sanity
#In place of [User_defined_name ]sanity we can use our own names (Ashok or Hello or any_name)

test_loginbyemail   -> Sanity, regression
test_loginbyfb      -> Sanity
test_loginbyphone   -> regression
test_signupbyemail  -> Sanity, regression
test_signupbyfb     -> regression
test_signupbyphone  -> Sanity
test_paymentindollor-> Sanity, regression
test_paymentinrupees-> regression

When you run the module it will give all passed and also some warnings.
Warnings are coming from decorators (User defined markers - @pytest.mark.sanity or regression).
To Avoid warnings we have to simply define user defined markers (sanity, regression) by creating *.ini file
*.ini should be in the same directory.
"""
import pytest

@pytest.mark.Sanity
@pytest.mark.regression
def test_loginbyemail():
    print("this is login by email test")
    assert 1 == 1

@pytest.mark.Sanity
def test_loginbyfb():
    print("this is login by facebook test")
    assert 1 == 1

@pytest.mark.regression
def test_loginbyphone():
    print("this is login by phone test")
    assert 1 == 1

@pytest.mark.Sanity
@pytest.mark.regression
def test_signupbyemail():
    print("this is signup by email test")
    assert 1 == 1

@pytest.mark.regression
def test_signupbyfb():
    print("this is signup by facebook test")
    assert 1 == 1

@pytest.mark.Sanity
def test_signupbyphone():
    print("this is signup by phone test")
    assert 1 == 1

@pytest.mark.Sanity
@pytest.mark.regression
def test_paymentindollor():
    print("This is payment in dollar test")
    assert True == True

@pytest.mark.regression
def test_paymentinrupees():
    print("This is payment in rupees test")
    assert True == True

"""
If you run complete file using below command:
python -m pytest PytestWithPython/test_demo8_grouping.py -s -v

Output:

collected 8 items                                                                                                                                   

PytestWithPython/test_demo8_grouping.py::test_loginbyemail this is login by email test
PASSED
PytestWithPython/test_demo8_grouping.py::test_loginbyfb this is login by facebook test
PASSED
PytestWithPython/test_demo8_grouping.py::test_loginbyphone this is login by phone test
PASSED
PytestWithPython/test_demo8_grouping.py::test_signupbyemail this is signup by email test
PASSED
PytestWithPython/test_demo8_grouping.py::test_signupbyfb this is signup by facebook test
PASSED
PytestWithPython/test_demo8_grouping.py::test_signupbyphone this is signup by phone test
PASSED
PytestWithPython/test_demo8_grouping.py::test_paymentindollor This is payment in dollar test
PASSED
PytestWithPython/test_demo8_grouping.py::test_paymentinrupees This is payment in rupees test
PASSED
================================================================ 8 passed in 0.11s 

Run only sanity test:
python -m pytest PytestWithPython/test_demo8_grouping.py -s -v -m "Sanity"

Output:
collected 8 items / 3 deselected / 5 selected                                                                                                       

PytestWithPython\test_demo8_grouping.py::test_loginbyemail this is login by email test
PASSED
PytestWithPython\test_demo8_grouping.py::test_loginbyfb this is login by facebook test
PASSED
PytestWithPython\test_demo8_grouping.py::test_signupbyemail this is signup by email test
PASSED
PytestWithPython\test_demo8_grouping.py::test_signupbyphone this is signup by phone test
PASSED
PytestWithPython\test_demo8_grouping.py::test_paymentindollor This is payment in dollar test
PASSED

========================================================= 5 passed, 3 deselected in 0.21s
Run only regression test:
 python -m pytest PytestWithPython/test_demo8_grouping.py -s -v -m "regression"

output:
collected 8 items / 2 deselected / 6 selected                                                                                                       

PytestWithPython\test_demo8_grouping.py::test_loginbyemail this is login by email test
PASSED
PytestWithPython\test_demo8_grouping.py::test_loginbyphone this is login by phone test
PASSED
PytestWithPython\test_demo8_grouping.py::test_signupbyemail this is signup by email test
PASSED
PytestWithPython\test_demo8_grouping.py::test_signupbyfb this is signup by facebook test
PASSED
PytestWithPython\test_demo8_grouping.py::test_paymentindollor This is payment in dollar test
PASSED
PytestWithPython\test_demo8_grouping.py::test_paymentinrupees This is payment in rupees test
PASSED

========================================================= 6 passed, 2 deselected in 0.18s 

Run both Sanity & regression test:
python -m pytest PytestWithPython/test_demo8_grouping.py -s -v -m "Sanity and regression"

Output:
collected 8 items / 5 deselected / 3 selected                                                                                                       

PytestWithPython\test_demo8_grouping.py::test_loginbyemail this is login by email test
PASSED
PytestWithPython\test_demo8_grouping.py::test_signupbyemail this is signup by email test
PASSED
PytestWithPython\test_demo8_grouping.py::test_paymentindollor This is payment in dollar test
PASSED

========================================================= 3 passed, 5 deselected in 0.17s 

Run only Sanity tests which are not belongs to regression:
python -m pytest PytestWithPython/test_demo8_grouping.py -s -v -m "Sanity" -m "not regression"

Output:
collected 8 items / 6 deselected / 2 selected                                                                                                        

PytestWithPython\test_demo8_grouping.py::test_loginbyfb this is login by facebook test
PASSED
PytestWithPython\test_demo8_grouping.py::test_signupbyphone this is signup by phone test
PASSED

========================================================= 2 passed, 6 deselected in 0.07s
Run only Sanity tests which are not belongs to regression:
python -m pytest PytestWithPython/test_demo8_grouping.py -s -v -m "regression" -m "not Sanity"

Output:
collected 8 items / 5 deselected / 3 selected                                                                                                       

PytestWithPython\test_demo8_grouping.py::test_loginbyphone this is login by phone test
PASSED
PytestWithPython\test_demo8_grouping.py::test_signupbyfb this is signup by facebook test
PASSED
PytestWithPython\test_demo8_grouping.py::test_paymentinrupees This is payment in rupees test
PASSED

========================================================= 3 passed, 5 deselected in 0.08s
"""