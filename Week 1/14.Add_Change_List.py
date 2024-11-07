# Changing List Item
'''
Lists are mutable, meaning their elements can be changed unlike string or tuple.

We can use the assignment operator = to change an item or a range of items.
'''

mylist = ["car", "table", "book", "floor", "mice", "washer", "pen"]

# change the first item
mylist[4] = 56
#print(mylist)

# change 2nd to 4th items
mylist[1:4] = ["boar", "lion", "cheeteh"]
#print(mylist)


'''
Adding to a list item

We can add one item to a list using the append() method or add several items using the extend() method.
'''
mylist = ["car", "table", "book", "floor"]

mylist.append("goat")
#print(mylist)

mylist.extend(["mice", "washer", "cheeteh"])
#print(mylist)

'''
Insert Items
To insert a list item at a specified index, use the insert() method.

The insert() method inserts an item at the specified index:
'''
# Insert an item as the second position:

thislist = ["apple", "banana", "cherry"]
thislist.insert(3, "orange")
print(thislist)

# Note: As a result of the examples above, the lists will now contain 4 items.
