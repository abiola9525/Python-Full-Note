# Booleans Data Type represent one of two values: True or False.
'''
In programming you often need to know if an expression is True or False.

You can evaluate any expression in Python, and get one of two answers, True or False.

When you compare two values, the expression is evaluated and Python returns the Boolean answer:
'''
#
print(10 > 9)
print(10 == 9)
print(10 < 9)
#

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

'''
# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return,
# '''
print(bool("Hello"))
print(bool(15))

#
# '''
# Most Values are True
# Almost any value is evaluated to True if it has some sort of content.
#
# Any string is True, except empty strings.
#
# Any number is True, except 0.
#
# Any list, tuple, set, and dictionary are True, except empty ones.'''
#
v = bool("xyz")
w = bool(576)
x = bool(["apple", "cherry", "banana"])
y = bool({"apple", "cherry", "banana"})
z = bool(("apple", "cherry", "banana"))

print(v)
print(w)
print(x)
print(y)
print(z)
#
# '''
# Some Valus are False
#
# There are not many values that evaluate to False, except empty values, such as empty list, empty tuple, empty set, empty string, the number 0, and the value None.
# And the value False evaluates to False.
# '''
#
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


# To check if an object is an integer or not:

x = 200
print(isinstance(x, int))

# To check if an object is an string or not:

x = "Python"
print(isinstance(x, int))
