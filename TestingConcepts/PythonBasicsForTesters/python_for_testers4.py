"""
Set:
1. it is unordered
2. can not have duplicate values
3. Sets are mutable
4. can store different data types
5. slicing is not possible
"""

demo_set = {10, "10", "Ashok"}
print(demo_set)
demo_set2 = set(("10", 20, "Kumar"))
print(demo_set2)
demo_set3 = {10, "10", "Ashok", 10, "10", "Ashok"}
print(demo_set) # removes duplicate
print(len(demo_set)) # removes duplicate and gives count

"""-------------------------Python Set Methods----------------------------------
add(x) - add element x to the set.
remove(x) - Removes element x from the set. Raise keyerror if x is not contained in the set
discard(x) - Remove element x from the set if it is present.
pop() - Remove and return an arbitrary element from the set. Raises keyerror if the set is empty.

Joining two sets:
union()
update()

Keep only duplicates
symmetric_difference()
symmetric_difference_update()

Returns set containing differenece between two or more sets:
difference()
difference_update()

issubset()
issuperset()
"""
print("------------------------Python Set Methods--------------------------------")

demo_set1 = {"Delhi", "Kolkata", "Hyderabad"}
demo_set2 = {"Delhi", "Kolkata", "Hyderabad", "Chennai", "Bengaluru"}
print(demo_set1)
demo_set1.add("Gujarat")
print(demo_set1)
demo_set1.remove("Delhi")
print(demo_set1)
demo_set1.discard("Kolkata")
print(demo_set1)
demo_set1.pop()
print(demo_set1)

demo_set1 = {"Delhi", "Kolkata", "Hyderabad"}
demo_set2 = {"Delhi", "Kolkata", "Hyderabad", "Chennai", "Bengaluru"}
demo_set3 = demo_set1.union(demo_set2)
print(demo_set3)
demo_set1.update(demo_set2) # Update didn't return value so we no need to create object
print(demo_set1)


demo_set1 = {"Delhi", "Kolkata", "Hyderabad"}
demo_set2 = {"Delhi", "Kolkata", "Hyderabad", "Chennai", "Bengaluru"}
demo_set3 = demo_set1.symmetric_difference(demo_set2)
print(demo_set3)
demo_set1.symmetric_difference_update(demo_set2) # Update didn't return value so we no need to create object
print(demo_set1)

demo_set1 = {"Delhi", "Kolkata", "Hyderabad"}
demo_set2 = {"Delhi", "Kolkata", "Hyderabad", "Chennai", "Bengaluru"}
# demo_set3 = demo_set1.difference(demo_set2)
demo_set3 = demo_set2.difference(demo_set1)
print(demo_set3)
# demo_set1.difference_update(demo_set2)
demo_set2.difference_update(demo_set1) # Update didn't return value so we no need to create object
print(demo_set2)

demo_set1 = {"Delhi", "Kolkata", "Hyderabad"}
demo_set2 = {"Delhi", "Kolkata", "Hyderabad", "Chennai", "Bengaluru"}
demo_set3 = demo_set1.issubset(demo_set2)
print(demo_set3)
demo_set1.issuperset(demo_set2) # Update didn't return value so we no need to create object
print(demo_set1)