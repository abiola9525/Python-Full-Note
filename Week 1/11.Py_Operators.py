'''
Operators are special symbols in Python that carry out arithmetic or logical computation.
The value that the operator operates on is called the operand
'''
x = 2+3
print(x)

# Here, + is the operator that performs addition.
# 2 and 3 are the operands and 5 is the output of the operation.

'''
Arithmetic Operators

Arithmetic operators are used to performing mathematical operations like addition, subtraction, multiplication, and division.

Operator	    Description	                                                                                     Syntax

+	            Addition: adds two operands	                                                                     x + y
–	            Subtraction: subtracts two operands	                                                             x – y
*	            Multiplication: multiplies two operands                                                          x * y
/	            Division (float): divides the first operand by the second	                                     x / y
//	            Division (floor): divides the first operand by the second	                                     x // y
%	            Modulus: returns the remainder when the first operand is divided by the second	                 x % y
**	            Power: Returns first raised to power second	                                                     x ** y

'''
#
# # Examples of Arithmetic Operator
a = 11
b = 3

# # Addition of numbers
add = a + b

# # Subtraction of numbers
sub = a - b

# # Multiplication of number
mul = a * b

# # Division(float) of number
div1 = a / b
#
# # Division(floor) of number
div2 = a // b
#
# # Modulo of both number
mod = a % b
#
# # Power
p = a ** b
#
# # print results
print(add)
print(sub)
print(mul)
print(div1)
print(div2)
print(mod)
print(p)



#
# '''
# Comparison Operators
# Comparison of Relational operators compares the values. It either returns True or False according to the condition.
#
# Operator	    Description	                                                                                        Syntax
#
# >	Greater than: True if the left operand is greater than the right	                                            x > y
# <	Less than: True if the left operand is less than the right	                                                    x < y
# ==	Equal to: True if both operands are equal	                                                                    x == y
# !=	Not equal to – True if operands are not equal	                                                                x != y
# >=	Greater than or equal to True if the left operand is greater than or equal to the right	                        x >= y
# <=	Less than or equal to True if the left operand is less than or equal to the right	                            x <= y
# is 	x is the same as y	                                                                                            x is y
# is not	x is not the same as y	                                                                                    x is not y
#
# N.B
#     = is an assignment operator and == comparison operator.
# '''
#
# # Examples of Comparision Operators
a = 15
b = 35

# a > b is False
print(a > b)

# a < b is True
print(a < b)

# a == b is False
print(a == b)

# a != b is True
print(a != b)

# a >= b is False
print(a >= b)

# a <= b is True
print(a <= b)

#

#
'''
Logical Operators
Logical operators perform Logical AND, Logical OR, and Logical NOT operations. It is used to combine conditional statements.

Operator	    Description	                                                        Syntax

and	            Logical AND: True if both the operands are true	                    x and y
or	            Logical OR: True if either of the operands is true 	                x or y
not	            Logical NOT: True if the operand is false 	                        not x
'''

# # Examples of Logical Operator
a = True
b = False

# Print a and b is False
print(a and b)

# Print a or b is True
print(a or b)

# Print not a is False
print(not a)

#
'''
Assignment Operators
Assignment operators are used to assign values to the variables.

Operator	    Description	                                                                                                        Syntax
=	            Assign value of right side of expression to left side operand 	                                                    x = y + z
+=	            Add AND: Add right-side operand with left side operand and then assign to left operand	                            a+=b     a=a+b
-=	            Subtract AND: Subtract right operand from left operand and then assign to left operand	                            a-=b     a=a-b
*=	            Multiply AND: Multiply right operand with left operand and then assign to left operand	                            a*=b     a=a*b
/=	            Divide AND: Divide left operand with right operand and then assign to left operand	                                a/=b     a=a/b
%=	            Modulus AND: Takes modulus using left and right operands and assign the result to left operand	                    a%=b     a=a%b
//=	            Divide(floor) AND: Divide left operand with right operand and then assign the value(floor) to left operand	        a//=b     a=a//b
**=	            Exponent AND: Calculate exponent(raise power) value using operands and assign value to left operand	                a**=b     a=a**b
&=	            Performs Bitwise AND on operands and assign value to left operand	                                                a&=b     a=a&b
|=	            Performs Bitwise OR on operands and assign value to left operand	                                                a|=b     a=a|b
^=	            Performs Bitwise xOR on operands and assign value to left operand	                                                a^=b     a=a^b
>>=	            Performs Bitwise right shift on operands and assign value to left operand	                                        a>>=b     a=a>>b
<<=	            Performs Bitwise left shift on operands and assign value to left operand	                                        a <<= b     a= a << b

'''

# Examples of Assignment Operators
a = 10

# Assign value
b = a
print(b)

# Add and assign value
b += a    #b = b + a
print(b)

# Subtract and assign value
b -= a
print(b)

# multiply and assign
b *= a
print(b)

# bitwise lishift operator
b <<= a
print(b)
