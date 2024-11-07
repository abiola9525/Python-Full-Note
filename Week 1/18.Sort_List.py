'''
Sort List Alphanumerically
List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

Sort the list alphabetically:
'''
mylist = ["car", "table", "book", "floor", "mice", "washer", "pen"]
mylist.sort()
print(mylist)


# Sort the list numerically:

mylist = [100, 50, 23, 82, 64]
mylist.sort()
print(mylist)

# '''
# Sort Descending
# To sort descending, use the keyword argument reverse = True:
# # '''
mylist = ["car", "table", "book", "floor", "mice", "washer", "pen"]
mylist.sort(reverse = True)
print(mylist)

#
# # Sort the list descending:
mylist = [100, 50, 23, 82, 64]
mylist.sort(reverse = True)
print(mylist)
