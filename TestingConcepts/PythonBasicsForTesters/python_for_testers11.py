"""
Inbuilt Functions:
max(): Returns the largest item in an iterable
min(): Returns the smallest item in an iterable
iter(): Returns an iterator object
reversed(): Returns a reversed iterator
next(): Returns the next item in an iterable
slice(): Returns a slice object
sorted(): Returns a sorted list
sum(): Sums the items of an iterator
input(): Allows user to input value.
"""

nums = [10, 29, 30, 1, 20, 4, 30]
print("----------Min()------------")
x = min(nums)
print(x)

print("----------Max()------------")
x = max(nums)
print(x)

print("----------iter(), next()------------")
x = iter(nums)
print(next(x))
print(next(x))
print(next(x))

print("----------reversed()------------")
nums = [10, 29, 30, 1, 20, 4, 30]
x = list(reversed(nums))
print(x)

print("----------slice()------------")
nums = [10, 29, 30, 1, 20, 4, 30]
x = slice(1, 6, 2)
print(nums[x])

print("----------sorted()------------")
nums = [10, 29, 30, 1, 20, 4, 30]
x = sorted(nums)
print(x)

print("----------sum()------------")
nums = [10, 29, 30, 1, 20, 4, 30]
x = sum(nums)
print(x)

print("----------input()------------")
nums = int(input("Enter number: "))
lis = []
for i in range(nums):
    lis.append(i)
print(lis)