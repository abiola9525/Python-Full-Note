'''
myset = {"apple", "banana", "cherry"}
Set
Sets are used to store multiple items in a single variable.
A set is a collection which is both unordered and unindexed.

Sets are written with curly brackets.
'''

# Create a Set:

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Note: Sets are unordered, so you cannot be sure in which order the items will appear.


'''
Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.

Unordered
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Unchangeable
Sets are unchangeable, meaning that we cannot change the items after the set has been created.

Once a set is created, you cannot change its items, but you can add new items.

Duplicates Not Allowed
Sets cannot have two items with the same value.
'''

# Duplicate values will be ignored:

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

'''
Get the Length of a Set
To determine how many items a set has, use the len() method.

Get the number of items in a set:
'''
thisset = {"apple", "banana", "cherry"}

print(len(thisset))


# A set can contain different data types:
set1 = {"abc", 34, True, 40, "male"}
print(set1)


'''
The set() Constructor
It is also possible to use the set() constructor to make a set.

Using the set() constructor to make a set:
'''

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
