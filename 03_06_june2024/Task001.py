
#1.Explain the difference between the = operator and the == operator in python


# Operator (Assignment Operator)
#Purpose: The = operator is used to assign a value to a variable.
#Usage: It sets the variable on the left-hand side to the value or expression on the right-hand side.

#Example
x = 5  # Assigns the value 5 to the variable x
y = x  # Assigns the value of x (which is 5) to the variable y

#In this example, x is assigned the value 5, and then y is assigned the value of x.

# == Operator (Equality Operator)
#Purpose: The == operator is used to compare two values for equality.
#Usage: It returns True if the values on the left-hand side and the right-hand side are equal,and False otherwise.

a = 10
b = 20
result = (a == b)  # Compares the value of a and b, result will be False because 10 is not equal to 20
print(result)  # Outputs: False

c = 10
result = (a == c)  # Compares the value of a and c, result will be True because both are 10
print(result)  # Outputs: True

#In this example, a == b evaluates to False because 10 is not equal to 20, whereas a == c evaluates to True because both a and c are 10.


#Summary of Differences:

#Function:

#= is used for assigning values to variables.
#== is used for comparing two values to check if they are equal.
#Context:

#= is used in statements where variables are being initialized or updated.
#== is used in expressions that perform a comparison and return a boolean value (True or False).
#Example to Highlight the Difference:
#Consider the following example that uses both operators:

#Example
x = 5  # Assignment
y = 10

if x == y:  # Comparison
    print("x and y are equal")
else:
    print("x and y are not equal")
#In this example:

#x = 5 assigns the value 5 to x.
#if x == y compares x and y. Since x (which is 5) is not equal to y (which is 10), the else block will execute, printing "x and y are not equal".

#2.What does the ** opeartor do in python and how it is used?

#1. Exponentiation (Mathematical Use)
#The ** operator is used to perform exponentiation, which means raising a number to the power of another number.

#Syntax:
#base ** exponent
#Example:

result = 2 ** 3  # 2 raised to the power of 3
print(result)  # Outputs: 8

result = 5 ** 2  # 5 raised to the power of 2
print(result)  # Outputs: 25


#What does the ^ operator in python ,and in what context it is commonly used?

"""
The ^ operator in Python is the bitwise XOR operator.
It performs an XOR operation on corresponding bits of two integers.
It is commonly used for bit manipulation tasks such as toggling bits, swapping variables without a temporary variable, and finding unique elements in a list.
"""