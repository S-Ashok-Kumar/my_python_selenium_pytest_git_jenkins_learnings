"""
if, elif, else
"""
print("----------------------if, elif, else-----------------------")
score = 85
if score > 90:
    print("I get motorbike")
elif 80 < score < 90:
    print("I will get bycycle")
else:
    print("you don't get anything")

"""
Loops: while loop
1. Used to iterate block of code as long as the condition is true
2. Can iterate on list, strings, tuples, dictionary
Syntax:
 while condition:
    body of loop
"""
print("----------------------While Loop-----------------------")
x = 0
while x<=10:
    print(x, end=" ")
    x += 1

"""
Break: Breaks out from the nearest enclosing loop.
       Whatever the statements after break will be skipped and also exit from the loop.
Continue: Go to the start of nearest enclosing loop
          Whatever the statements satisfies the condition, will be skipped and Continues to print remaining statements.

While condition:
    statement1
    break
    statement2
    continue
    statement3
    
else clause:
while condition:
    statements
else:
    statements
"""
print("\n----------------------Break EX-----------------------")
x = 0
while x<=10:
    if x == 5:
        x += 1
        break
    else:
        print(x)
    x += 1
print("Outside the while loop")


print("----------------------Continue EX-----------------------")
x = 0
while x<=10:
    if x == 5:
        x += 1
        continue
    else:
        print(x)

    x += 1
print("Outside the while loop")

"""
Zip Function: 
1. The zip() function returns an iterator of tuples, where each tuple contains elements from the input iterables.
2. It Returns the iterator.
3. iterable means anything you can loop through in python String, list, set, tuple, dictionary, range(), even generators 
4. It will map 1 to 1 from the 2 iterables
"""
print("----------------------Zip EX-----------------------")

lis1 = ["India", "USA", "UK"]
lis2 = ["Bengaluru", "Texas", "London"]
res1 = list(zip(lis1, lis2))
res2 = dict(zip(lis1, lis2))
res3 = tuple(zip(lis1, lis2))
res4 = set(zip(lis1, lis2))
print(res1)
print(res2)
print(res3)
print(res4)
print()

# Different iterables
a = [1, 2, 3]              # list
b = ('a', 'b', 'c')        # tuple
c = 'XYZ'                  # string
result = list(zip(a, b, c))
print(result,"\n")

# With Range and Set
result = list(zip(range(3), {10, 20, 30}))
print(result,"\n")

# With Dictionary Keys or Values
d1 = {'a': 1, 'b': 2}
d2 = {'x': 10, 'y': 20}
print(list(zip(d1, d2)))         # keys zipped
print(list(zip(d1.values(), d2.values())))


"""
For Loop:
1. Used to iterate block of code as long as the condition is true
2. Mostly used when we know where the condition ends

Else with for Loop:
1. The else block runs only if the loop finishes normally (i.e. no break happens).
2. If the loop is terminated early by break, the else block is skipped.

Range:
Syntax: range(start, stop, step)
1. Range is built-in function.
2. It generates the sequence of numbers.
"""
print("----------------------For Loop EX-----------------------")

for i in range(11):
    print(i, end=" ")
print()

nam = "Ashok Kumar"
for i in nam:
    print(i)

print("----------------------Else with For Loop EX-----------------------")
# Without break statement
for i in range(5):
    print(i)
else:
    print("Loop completed normally!")


# With break statement
print()
for i in range(5):
    if i == 3:
        print("Breaking the loop at", i)
        break
    print(i)
else:
    print("Loop completed normally!")

#Real use case where we use else with for
print()
numbers = [2, 4, 6, 8, 10]

for n in numbers:
    if n == 7:
        print("Found 7!")
        break
else:
    print("7 not found in the list.")

