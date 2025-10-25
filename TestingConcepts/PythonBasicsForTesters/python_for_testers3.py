"""
List:
1. Mutable
2. stores duplicate values
3. slicing is possible
4. Can store different data types
"""
from operator import index

lis = ["Ashok", 25, 5.8, 25]
print(lis[1])
print(type(lis))
print(lis[0:2])

"""-------------------------Python List Methods----------------------------------
list.append(x) - add item at the end of the list
list.insert(i,x) - Insert an item at a given index
list.remove(x) - Remove the first item from the list whose value is equal to x
list.pop([i]) - remove the item at the given position in the list, and return it.
                If no index is specified, a.pop() removes and returns the last item in the list
list.index(x[, start[, end]]) - return zero-based index in the list of the first item whose value is equal to x.
list.count(x) - Return the number of times x appears in the list
list.sort(*, key=None, reverse=False) - sort the item of the list in place
list.reverse() - reverse the elements of the list in place
list.copy() - Return a shallow copy of the list. Equivalent to a[:].
list.clear() - Removes all items from the list. Equivalent to del a[:]
"""
print("------------------------Python List Methods--------------------------------")

cities = ["Delhi", "Mumbai", "Hyderabad", "Kolkata"]
cities.append("Chennai")
print(cities)
cities.insert(0, "Bengaluru")
print(cities)
cities.remove("Hyderabad")
print(cities)
cities.pop(1)
print(cities)
print(cities.index("Kolkata"))
print(cities.count("Mumbai"))
cities.sort()
print(cities)
cities.reverse()
print(cities)
new_cities = cities.copy()
print(new_cities)
final_list = new_cities.clear()
print(final_list)
