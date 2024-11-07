'''
Python Functions
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

Creating a Function
In Python a function is defined using the def keyword:
'''
#   Example
def my_function():
  print("Hello from a function")
#Calling a Function
#To call a function, use the function name followed by parenthesis:

#Example
def my_function():
  print("Hello from a function")

my_function()

'''Your code defines a function square that squares its input, and then it applies this function to each element in the numbers list using a list comprehension. Here's a step-by-step breakdown:

python
Copy code
def square(x):
    return x**2

numbers = [1, 2, 3, 4, 5]
squared_numbers = [square(x) for x in numbers]
print(squared_numbers)'''
