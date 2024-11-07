'''
In Python, object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming.
It aims to implement real-world entities like inheritance, polymorphisms, encapsulation, etc. in the programming. 
The main concept of OOPs is to bind the data and the functions that work on that together as a single unit so that no other part of the code can access this data.

Main Concepts of Object-Oriented Programming (OOPs) 
    Class
    Objects
    Polymorphism
    Encapsulation
    Inheritance
    Data Abstraction
'''

# Polymorphism
# Polymorphism simply means having many forms. For example, we need to determine if the given species of birds fly or not, using polymorphism we can do this using a single function.

# Example: Polymorphism in Python

class Bird:
   
    def intro(self):
        print("There are many types of birds.")
 
    def flight(self):
        print("Most of the birds can fly but some cannot.")
 
class sparrow(Bird):
   
    def flight(self):
        print("Sparrows can fly.")
 
class ostrich(Bird):
 
    def flight(self):
        print("Ostriches cannot fly.")
 
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
 
obj_bird.intro()
obj_bird.flight()
 
obj_spr.intro()
obj_spr.flight()
 
obj_ost.intro()
obj_ost.flight()


'''
Encapsulation
Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). 
It describes the idea of wrapping data and the methods that work on data within one unit. 
This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. 
To prevent accidental change, an object’s variable can only be changed by an object’s method. 
Those types of variables are known as private variables.

A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.
'''
Example: Encapsulation in Python

# Python program to
# demonstrate private members
 
# Creating a Base class
class Base:
    def __init__(self):
        self.a = "PlatformLead"
        self.__c = "PlatformLead"
 
# Creating a derived class
class Derived(Base):
    def __init__(self):
 
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)
 
 
# Driver code
obj1 = Base()
print(obj1.a)

'''
Comprehensions in Python provide us with a short and concise way to construct new sequences (such as lists, set, dictionary etc.) using sequences which have been already defined. Python supports the following 4 types of comprehensions:

    List Comprehensions
    Dictionary Comprehensions
    Set Comprehensions
    Generator Comprehensions

List Comprehensions:

List Comprehensions provide an elegant way to create new lists. The following is the basic structure of a list comprehension:

    output_list = [output_exp for var in input_list if (var satisfies this condition)]

Note that list comprehension may or may not contain an if condition. List comprehensions can contain multiple for (nested list comprehensions).

'''
# Suppose we want to create an output list which contains only the even numbers which are present in the input list. 
# Let’s see how to do this using for loops and list comprehension and decide which method suits better.
# Constructing output list WITHOUT Using List comprehensions
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
  
output_list = []
# Using loop for constructing output list
for var in input_list:
    if var % 2 == 0:
        output_list.append(var)  
print("Output List using for loop:", output_list)



# Using List comprehensions
# for constructing output list
  
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

list_using_comp = [var for var in input_list if var % 2 == 0]
print("Output List using list comprehensions:", list_using_comp)






#            Dictionary Comprehensions:
'''


Extending the idea of list comprehensions, we can also create a dictionary using dictionary comprehensions. The basic structure of a dictionary comprehension looks like below.

    output_dict = {key:value for (key, value) in iterable if (key, value satisfy this condition)}


Suppose we want to create an output dictionary which contains only the odd numbers that are present in the input list as keys and their cubes as values. 
Let\'s see how to do this using for loops and dictionary comprehension.
'''

input_list = [1, 2, 3, 4, 5, 6, 7]
  
output_dict = {}
  
# Using loop for constructing output dictionary
for var in input_list:
    if var % 2 != 0:
        output_dict[var] = var**3
  
print("Output Dictionary using for loop:", output_dict )



# Using Dictionary comprehensions for constructing output dictionary
  
input_list = [1,2,3,4,5,6,7]
  
dict_using_comp = {var:var ** 3 for var in input_list if var % 2 != 0}
  
print("Output Dictionary using dictionary comprehensions:", dict_using_comp)





# Generator Comprehensions are very similar to list comprehensions. 
# One difference between them is that generator comprehensions use circular brackets whereas list comprehensions use square brackets. 
# The major difference between them is that generators don’t allocate memory for the whole list. 
# Instead, they generate each value one by one which is why they are memory efficient. 
# Let’s look at the following example to understand generator comprehension:

input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
  
output_gen = (var for var in input_list if var % 2 == 0)
  
print("Output values using generator comprehensions:", end = ' ')
  
for var in output_gen:
    print(var, end = ' ')