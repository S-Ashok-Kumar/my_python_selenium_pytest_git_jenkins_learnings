"""
Command to Run:
python -m pytest PytestWithPython/test_demo10_parallel.py -s -v -n 2
                        or
python -m pytest PytestWithPython/test_demo10_parallel.py -s -v -n=2
-n = number of workers (helps to perform parallel testing.)
Maximum we can provide 5 workers. Then only execution will be faster.
If you mention more than 5 workers, it will execute slowly.

Pre-requisite: install pytest-xdist plugin
Command to install: pip install pytest-xdist
"""

def test_one():
    print("running test one")
    assert True

def test_two():
    print("running test two")
    assert True

def test_three():
    print("running test three")
    assert True

def test_four():
    print("running test four")
    assert True

"""
Output:

2 workers [4 items]     
scheduling tests via LoadScheduling

PytestWithPython\test_demo10_parallel.py::test_three
PytestWithPython\test_demo10_parallel.py::test_one
[gw0] PASSED PytestWithPython\test_demo10_parallel.py::test_one
PytestWithPython\test_demo10_parallel.py::test_two
[gw0] PASSED PytestWithPython\test_demo10_parallel.py::test_two
[gw1] PASSED PytestWithPython\test_demo10_parallel.py::test_three
PytestWithPython\test_demo10_parallel.py::test_four
[gw1] PASSED PytestWithPython\test_demo10_parallel.py::test_four

================================================================ 4 passed in 0.67
"""