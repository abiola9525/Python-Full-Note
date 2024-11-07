a = "Welcome"
b = "Home"
greet = a + b
print(greet)
#
# # To add a space in between them
# greet = a +' '+ b
# print(greet)

#
#
#           Formatting String

#
year = 2021
note = "My year of birth is " + year
print("My year of birth is ", year)
#
'''
But we can combine strings and numbers by using the format() method!
The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
'''
year = 2020
note = "My year of birth is {}"
print(note.format(year))

'''
The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
'''
# product = "Samsung"
# year = 2022
# price = 345.45
# myorder = "I want a brand of {} of year {} at a price range of ${}."
# print(myorder.format(product, year, price))


product = "Samsung"
year = 2022
price = 375.45
myorder = "I want a brand of {1} of year {2} at a price range of ${0}."
print(myorder.format(price, product, year))
