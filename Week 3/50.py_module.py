'''
What is a Module?

Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.
Create a Module

To create a module just save the code you want in a file with the file extension .py:
 '''
 
# Save this code in a file named mymodule.py
# def greeting(name):
#   print("Hello, " + name) 


import mymodule

mymodule.greeting("Jonathan")
# Note: When using a function from a module, use the syntax: module_name.function_name.



import mymodule

a = mymodule.person1["age"]
print(a) 



'''
# Re-naming a Module

You can create an alias when you import a module, by using the as keyword:

Create an alias for mymodule called mx:'''

import mymodule as mx

a = mx.person1["age"]
print(a) 

'''
Built-in Modules

There are several built-in modules in Python, which you can import whenever you like.

Import and use the platform module:
'''
import platform

x = platform.system()
print(x) 