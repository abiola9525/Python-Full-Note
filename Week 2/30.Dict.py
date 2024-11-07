'''Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
Dictionaries are written with curly brackets, and have keys and values:
'''
#Example:  Create and print a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print("=================================")
this dict#                   Accessing Items
#You can access the items of a dictionary by referring to its key name, inside square brackets:

#Example:  Get the value of the "model" key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
#There is also a method called get() that will give you the same result:
print("=================================")
#Example:   Get the value of the "model" key:
x = thisdict.get("model")
print(x)

print("=================================")
#Get a list of the keys:
x = thisdict.keys()
print(x)
# The keys() method will return a list of all the keys in the dictionary.
# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
print("=================================")
# Add a new item to the original dictionary, and see that the keys list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change
print("=================================")
car["color"] = "white"

print(x) #after the change
print("=================================")
#Get a list of the values:

x = thisdict.values()
# The values() method will return a list of all the values in the dictionary.
print("=================================")
# Make a change in the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change
print("=================================")
car["year"] = 2020

print(x) #after the change
print("=================================")
# Add a new item to the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change
print("=================================")
car["color"] = "red"

print(x) #after the change
print("=================================")
#Get a list of the key:value pairs

x = thisdict.items()
# The items() method will return each item in a dictionary, as tuples in a list.
print("=================================")
# Make a change in the original dictionary, and see that the items list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change
print("222222=================================")
car["year"] = 2020

print(x) #after the change
print("=================================")

#Add a new item to the original dictionary, and see that the items list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change
print("=================================")
car["color"] = "red"

print(x) #after the change

print("=================================")
'''
To determine if a specified key is present in a dictionary use the in keyword:

Example
Check if "model" is present in the dictionary:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

print("=================================")















