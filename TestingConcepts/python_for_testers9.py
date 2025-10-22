"""
Positional Arguments
Keyword Arguments
Required Arguments
Optional Arguments

Parameters:
    1. Definition: Parameters are placeholders or variables that a function defines to receive input.
    2. Where used: In the function definition.
Arguments:
    1. Definition: Arguments are the actual values you pass to a function when calling it.
    2. Where used: In the function call.
"""

print("----------------Positional Arguments------------------")
# Positional Arguments
def add(x, y):  # x and y are parameters
    return x + y

result = add(5, 6)  # 5 and 6 are arguments
print(result)


print("----------------Keyword Arguments------------------")
# Positional Arguments
def add(x, y):  # x and y are parameters
    return x - y

result = add(y=6, x=5)  # 5 and 6 are arguments
print(result)

print("----------------Required Arguments------------------")
def multiply(a, b):
    return a * b

print(multiply(5, 2))  # Works
# print(multiply(5))    # Error: missing 1 required positional argument: 'b'

print("----------------optional Arguments------------------")
def text(a, b= "Good Morning!!"):
    return a+ " " +b

print(text("Ashok")) # Uses default message
print(text("Hello", "How are you!" ))  # Overrides default
