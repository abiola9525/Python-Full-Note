'''
Arguments
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses.
You can add as many arguments as you want, just separate them with a comma.

The following example has a function with one argument (fname).
When the function is called, we pass along a first name, which is used inside the function to print the full name:

Arguments are often shortened to "args" in Python documentations.
'''

# Example
def my_function(fname):
  print(fname + " Junior")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

print("============================")
'''
Parameters or Arguments?
The terms parameter and argument can be used for the same thing: information that are passed into a function.

From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.
'''

'''
Number of Arguments
By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

Example
This function expects 2 arguments, and gets 2 arguments:
'''
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
#If you try to call the function with 1 or 3 arguments, you will get an error
print("============================")
'''
1.           Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:
'''
# Example:   If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
print("============================")
'''
2.           Keyword Arguments
You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter.
'''
# Example
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
# The phrase Keyword Arguments are often shortened to kwargs in Python documentations.
print("============================")

'''
3.                Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:
'''
# Example:   If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
# Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.
print("============================")

'''
                Default Parameter Value
The following example shows how to use a default parameter value.

If we call the function without argument, it uses the default value:

Example
'''
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
print("============================")

'''
                Passing a List as an Argument
You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

E.g. if you send a List as an argument, it will still be a List when it reaches the function:

Example
'''
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)













