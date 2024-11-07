  
    


"""   
#Scope
'''In Python,
there are two main types of variable scope: global scope and local scope.


Global Scope:
Variables defined outside of any function or block have a global scope.
They can be
accessed and modified from anywhere in the code, including inside functions.
'''

x = 10

def my_function():
    x = 10
    x = 12
    print(x)
my_function()
# Local Scope:
'''Variables defined inside a function have a local scope.
They can only be accessed and modified within that specific function.

''' """

mydict = { "A": [1,2,3,4,5,6,7,8,9],
            "B" :[2,4,6,8,10,12,14],
            "C" :[3,6,9,12,15,18,21]
            }


print(mydict.keys())
print(list(mydict.values()))

print(mydict.items())
print("__" *16)
List = (mydict.get("A"))

count = 1

while count <= len(List):
    series= List[-count]
    
    print(series, end =" ")

    count += 1

Listt = []

count = 0


        





































'''

class Dog:
    def __init__ (self, name): # self invisblely takes the referrence passed to the 
        self.name = name  #  Define an Atribute of the Class Dog name
        

y = Dog( "Femi")
print (y.name)













# the type we have defines what we are allowed to do with specfic Objectstring
string = "Hello"
x = 1

print(string.upper()) # method acting on a specific Object
print(string.upper()) # " int " as no attribute .upper()

# so, there different things we can do to this object is based on the type of class  dey are
'''
