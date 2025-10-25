"""
Tuples:
1. Allows duplicate values and cannot be modified (immutable)
2. Tuples are indexed
3. Can be stored different data types
4. slicing is possible
"""

demo_tuple = (1, 2, 3, "Ashok", 5.6, True, 1, 1, 2, 3)
demo_tuple1 = (100, "Kumar")
print(demo_tuple[3])
print(len(demo_tuple))

"""-------------------------Python Tuple Methods----------------------------------"""

print("------------------------Python Tuple Methods--------------------------------")
print(demo_tuple.count(1))
print(demo_tuple.index("Ashok"))
print(demo_tuple[3])
print(demo_tuple1+demo_tuple)
print(demo_tuple[0:5])