#1. Leap Year Checker:
#Create a program that determines whether a given year is a leap year.A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
#Use an if-else statement to make this determination.
#Input = 2024
#Output = Leap year
# year = int(input("Enter the year: "))
#
# if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 print("It is a leap year")
#             else:
#                 print("It is not a leap year")
#         else:
#             print("It is a leap year")










#2. Triangle Classifier:
#Write a program that classifies a triangle based on its side lengths.
#Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
#Use an if-else statement to classify the triangle.

#3 Input

#side 1, side 2 and side 3

#output - Eq, Iso, Scalene -

#Eq. = side 1 == side 2 = side 3
'''
side1=float(input("Enter the side 1 :"))
side2=float(input("Enter the side 2 :"))
side3=float(input("Enter the side 3 :"))

if side1==side2 and side2==side3:
    print(f"Triangle is equaliterial")
elif side1==side2 or side1==side3 or side2==side3:
    print("Isosceles")
else:
    print("scalene")'''








#Task - Fibonacci series and Factorial


# 3. Factorial

# n = 5

# 5! -->5*4*3*2*1 -> 120

# 3! -> 3*2*1 -> 6

# 4! -> 4*3*2*1 -> 24



#
# number=int(input("Enter the number"))
# factorial_result=1
# for i in range (1,number+1):
#  factorial_result*=i
#
# # Print the result
# print(f"The factorial of {number} is {factorial_result}.")


#4. Fibonaci series
# 0,0+1, 0+1+1,

# n = 7
#0 1 1 2
# 0, 1, 2, 3, 5, 8, 13

fibonaci_series=int(input("Enter the number"))
a, b = 0, 1
for i in range (0,fibonaci_series+1):
    print(a, end=" ")
    a,b=b ,a+b #(first_number+second number =second_number))


