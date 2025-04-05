# Basic systax
dictionary = {
    "apple" : "a fruit",
    "car" : "a vehicle",
    "book" : "something we read",
}

# print(dictionary["apple"])

# Common operation
dictionary["country"] = "Bangladesh" # add new item
dictionary["book"] = "read" # change value
# del dictionary["apple"]

# key checking
"""
if "apple" in dictionary:
    print("yes")
"""

# .get() methode
print(dictionary.get("apple", "not found"))

for key, value in dictionary.items():
    print(f'{key} -> {value}')

# nested dictionary
students = {
    "s1" : {"name" : "a", "age" : 21},
    "s2" : {"name" : "b", "age" : 30}
}

print(students["s2"]["name"])