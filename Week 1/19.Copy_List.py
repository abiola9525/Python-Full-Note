# The copy() method returns a shallow copy of the list.

'''
    copy() Syntax
The syntax of the copy() method is:
new_list = list.copy()

    copy() Parameters
The copy() method doesn't take any parameters.

    copy() Return Value
The copy() method returns a new list. It doesn't modify the original list.
'''

prime_numbers = [2, 3, 5]
numbers = prime_numbers.copy()
numbers.append("boy")
print(prime_numbers)
print('Copied List:', numbers)

'''
    List copy using =
We can also use the = operator to copy a list. For example,

Howerver, there is one problem with copying lists in this way. If you modify new_list, old_list is also modified. 
It is because the new list is referencing or pointing to the same old_list object.
'''
#
# old_list = [1, 2, 3]
# # copy list using =
# new_list = old_list
# # add an element to list
# new_list.append('a')
#
# print('New List:', new_list)
# print('Old List:', old_list)
# #
#
#
#
#  # Copy List Using Slicing Syntax
#
#
list = ['cat', 0, 6.7,54, 65, 86]
# copying a list using slicing
new_list = list[0:2]


# Adding an element to the new list
new_list.append('dog')

# Printing new and old list
print('Old List:', list)
print('New List:', new_list)
#



'''
Assingment

1. Create a program that will give out of all even number from 0 - 200
2.  Create a program that will give out of all odd number from 0 - 200
'''
