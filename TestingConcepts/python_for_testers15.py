"""
Exception Handling:

inputs:
25,0
28,2
"""
from logging import exception

try:    # Code that might cause an error goes inside the try block.
    print("first number: ")
    x = int(input())
    print("second number: ")
    y = int(input())
    if y == 0:
        raise exception("The denominator is 0")     # If we know the error before itself we can raise the exception
    print(x/y)
except Exception as e:  # Code to handle the error goes inside the except block.
    print("error is: ",e)
else:       # If there is any exception in the code then else block doesn't execute
    print("In else block")
finally:    # Even if we get exception or not, the finally will definitely execute
    print("Finally will always be executed")