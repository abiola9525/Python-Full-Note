'''
Removing Items
There are several methods to remove items from a dictionary:
1. pop() method
2. popitem() method
3. del method
4. clear() method
'''

#1. The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
print("============================")

#2. The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
print("============================")
#3. The del keyword removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

print("============================")
# The del keyword can also delete the dictionary completely:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.
print("============================")
#4. The clear() method empties the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)


'''
Using Enumerate:
If you need both the key and its index in the iteration, you can use enumerate():
'''

my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Iterate over keys and their index
for index, key in enumerate(my_dict):
    print(f'Index: {index}, Key: {key}')
