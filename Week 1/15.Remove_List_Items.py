'''
Remove Specified Item
The remove() method removes the specified item.
'''

# Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("cherry")
print(thislist)


'''
Remove Specified Index
The pop() method removes the specified index.

'''

# Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#
# # If you do not specify the index, the pop() method removes the last item.
#
#
# ''' The del keyword also removes the specified index:
#
#  Remove the first item:
# '''
thislist = ["apple", "banana", "cherry"]
del thislist[2]
# print(thislist)
#
# # The del keyword can also delete the list completely.
#
# # Delete the entire list:

thislist = ["apple", "banana", "cherry"]
del thislist
# print(thislist)
#
#
# '''
# Clear the List
# The clear() method empties the list.
#
# The list still remains, but it has no content.
#
# Clear the list content:
# '''
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
