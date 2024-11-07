'''
Access Tuple Items
You can access tuple items by referring to the index number, inside square brackets:
'''

# to print the third item in the tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple[2])

# Note: The first item has index 0.

'''
Negative Indexing
Negative indexing means start from the end.

-1 refers to the last item, -2 refers to the second last item etc.
'''

# print the second to the last item of the tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple[-2])


'''
Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new tuple with the specified items.
'''

# Return the third, fourth, and fifth item:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# Note: The search will start at index 2 (included) and end at index 5 (not included).


# This example returns the items from the beginning to, but NOT included, "kiwi":

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])


'''
Range of Negative Indexes
Specify negative indexes if you want to start the search from the end of the tuple:
'''
# This example returns the items from index -4 (included) to index -1 (excluded)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

'''
Check if Item Exists
To determine if a specified item is present in a tuple use the in keyword:
'''

# Check if "apple" is present in the tuple:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
if "kiwi" in thistuple:
  print("Yes, 'kiwi' is in the fruits tuple")
