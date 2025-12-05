"""
Command to run:
python -m pytest PytestWithPython/test_demo3_scope.py -s -v

***# Scope="function"  - The fixture runs before each test function and ends after that test.

                         Ex:
                            import pytest

                            @pytest.fixture(scope="function")
                            def setup_func():
                                print("\n[Setup Function]")
                                yield
                                print("[Teardown Function]")

                            def test_one(setup_func):
                                print("Test One")

                            def test_two(setup_func):
                                print("Test Two")

                        op:
                            [Setup Function]
                            Test One
                            [Teardown Function]

                            [Setup Function]
                            Test Two
                            [Teardown Function]


***# Scope="module"    - The fixture runs once per Python file (module)
                       - before the first test in that file, and after all tests are done.

                         Ex:
                            import pytest

                            @pytest.fixture(scope="module")
                            def setup_module():
                                print("\n[Setup Module]")
                                yield
                                print("[Teardown Module]")

                            def test_a(setup_module):
                                print("Test A")

                            def test_b(setup_module):
                                print("Test B")

                        op:
                            [Setup Module]
                            Test A
                            Test B
                            [Teardown Module]


# Scope="class"        - The fixture runs once per class, before any methods in that class, and after all are done.

                         Ex:
                            import pytest

                            @pytest.fixture(scope="class")
                            def setup_class():
                                print("\n[Setup Class]")
                                yield
                                print("[Teardown Class]")

                            class TestSample:
                                def test_x(self, setup_class):
                                    print("Test X")

                                def test_y(self, setup_class):
                                    print("Test Y")

                        op:
                            [Setup Class]
                            Test X
                            Test Y
                            [Teardown Class]


# Scope="session"      - The fixture runs only once per test session (entire run, across all test files).

                         Ex:
                            import pytest

                            @pytest.fixture(scope="session")
                            def setup_session():
                                print("\n[Setup Session]")
                                yield
                                print("[Teardown Session]")

                            def test_one(setup_session):
                                print("Test One")

                            def test_two(setup_session):
                                print("Test Two")

                        op:
                            [Setup Session]
                            Test One
                            Test Two
                            [Teardown Session]


Session -> Module -> CLass -> Methods   (If we use session)
Module -> CLass -> Methods              (If we use class)
Module -> Functions                     (If we don't use class)
"""
import pytest


# By default, fixture scope is a function scope.
# Try by changing scopes as module, class, session.
@pytest.fixture(scope="module")
def setup():
    print("Launch the browser")


def test_one(setup):
    print("this is my test one")


def test_two(setup):
    print("this is my test two")


def test_three(setup):
    print("this is my test three")


"""
Output: def setup(scope="function"):

collected 3 items                                                                                                                                    

PytestWithPython/test_demo3_scope.py::test_one Launch the browser
this is my test one
PASSED
PytestWithPython/test_demo3_scope.py::test_two Launch the browser
this is my test two
PASSED
PytestWithPython/test_demo3_scope.py::test_three Launch the browser
this is my test three
PASSED


Output: def setup(scope="module"):

collected 3 items                                                                                                                                    

PytestWithPython\test_demo3_scope.py::test_one Launch the browser
this is my test one
PASSED
PytestWithPython\test_demo3_scope.py::test_two this is my test two
PASSED
PytestWithPython\test_demo3_scope.py::test_three this is my test three
PASSED

================================================================ 3 passed in 0.16
"""
