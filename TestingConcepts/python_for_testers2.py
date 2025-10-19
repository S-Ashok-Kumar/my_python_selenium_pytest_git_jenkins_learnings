"""Compiler: Reads all the source code at once, checks for errors,
            and converts it into machine code if there are none.
Interpreter: Executes the code line by line, converting it into
            machine-readable instructions on the go, and stops immediately when an error occurs."""
"""
variable rules:
Starts with: A-Z, a-z, _
Cannot start with: 0-9, inbuilt keywords (as, and, break, class.....)
"""
import keyword
username = "Ashok"
print(username,type(username), id(username))

num = 8
print(num, type(num), id(num))

num = 30.2
print(num, type(num), id(num))

list_of_keywords = keyword.kwlist
print(list_of_keywords)

"""
Operators:
Arithemetic operators: +, -, *, /, %, **, //
Assignment operator: =, +=, -+, *=, /=, **=
Comparison operator: ==, !=, >=, <=, <, >
Logical operator: and, or
Identity operators: is, is not
Membership operators: in, not in
Bitwise operators: & or AND, | or OR, ~ or NOT, ^ or XOR
basically Bitwise operators work on binary numbers. Not used frequently.
"""
"""
BODMAS - Brackets (), Order **, Division / or //, Multiplication *, Addition +, Substraction -
"""
"""--------------STRINGS----------------"""
print("----------------String EX--------------------")
name = 'India'
print(name)

lap = 'choocha\'s Laptop'
print(lap)

lap = "choocha's Laptop"
print(lap)

# below 3 lines provide error, because string doesn't support assigning a value.
# alphabets = 'ABCDEGHI'
# alphabets[5] = 'F'
# print(alphabets)

alphabets = 'ABCDEGHI'
s = alphabets[-1]
print(s)

alphabets = 'ABCDEGHI'
s = alphabets[0:4]
print(s)

rstring = r'Hello world\nwelcome'
print(rstring)

"""--------------STRINGS Inbuilt Functions----------------
len(s), 
str(), 
upper(), lower()
count(sub[, start[, end]])
isupper(), islower(), 
split(sep=None, maxsplit=-1),
rsplit, 
strip(), lstrip([chars]), rstrip([chars]),
replace(old, new[, count]), 
find(sub[, start[, end]]),
index(sub[, start[, end]])
"""
print("----------------String Inbuilt Functions--------------------")
s = "     Ashok KumAr       "
n = 1234567
print(len(s))
z = str(n)
print(z)
print(z.find("56"))
print(s.upper())
print(s.count("a", 1, 10))
print(s.lower())
print(s.isupper())
print(s.islower())
print(s.split())
print(s.strip(" "))
print(s.lstrip(" "))
print(s.rstrip(" "))
print(s.replace("A", "a"))
print(s.replace("A", "a", 1))
print(s.find("A")) # Returns the lowest index in the data where the subsequence sub is found
print(s.index("A")) # Raise ValueError when the subsequence is not found

"""String Formatting------------------------------------------------"""
print("----------------String Formatting--------------------")
name = 'Johnny'
age = 55

print('Hi ' + name + '. You are ' + str(age) + ' years old')
print(f'Hi {name}. You are {age} years old')
print('Hi {}. You are {} years old'.format(name, age))
print('Hi {0}. You are {1} years old'.format(name, age))
print('Hi {1}. You are {0} years old'.format(name, age))
print('Hi {new_name}. You are {age} years old'.format(new_name='Nani', age=23))
