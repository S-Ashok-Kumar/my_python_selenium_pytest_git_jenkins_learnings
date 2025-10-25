"""
Dictionaries:
1. It stores data in key:value pairs.
2. They are changeable and do not allow duplicate values
3. It is mutable
"""

demo_dict = {1:20, "A":"Ashok", 2:5.7, "k":"Kumar", 1:20}
print(demo_dict)
print(demo_dict["A"])
demo_dict["r"] = "Rocky"
print(demo_dict)

"""-------------------------Python Dictionary Methods----------------------------------
get() - Returns the value for specifined key in the dictionary.
keys() - Returns a copy of dictionary's keys
items() - Returns a copy for dictionaries key value pair.
values() - Returns a copy of the values in the dictionary
pop() - Removes the item with the specified key. If not mentioned, removes the last element
popitem() - Removes the arbitary key:value pair
update() - Adds the specified key-value pairs to dictionary
copy() - Returns a copy of the dictionary
clear() - Removes all the elements from the dictionary.
"""


print("------------------------Python Dictionary Methods--------------------------------")
demo_dict1 = {"a":"Ashok", "b":"Banu", "c":"Chaitanya"}
print(demo_dict1.get("b"))
print(demo_dict1.keys())
print(demo_dict1.items())
print(demo_dict1.values())
print(demo_dict1.pop("b"))
print(demo_dict1.popitem())

demo_dict1.update({"d":"Dany"})
print(demo_dict1)
new_dict = demo_dict1.copy()
print(new_dict)
new_dict.clear()
print(new_dict)