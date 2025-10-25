"""
Functions:
A function is a block of reusable code that performs a specific task.
It is defined using def and can exist independently — not tied to any object.

Methods:
A method is a function that belongs to an object (like a list, string, or class instance).
It always operates on that object, and you call it using dot notation.
"""
print("---------------- Functions EX---------------------")
def add(x, y):
    return x+y

print(add(5, 6))


# def add(x, y):
#     print(x+y)
#
# add(5, 6)


print("---------------- Methods EX---------------------")
s = "ashok"
print(s.upper())    # upper is tied to the string object s. You can't call upper() directly.
