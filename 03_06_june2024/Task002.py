# #Task#2.
# #Develop a python script that calculate the square and cube of a given number
# #num=2 sq=4 ,c=8
# #Square of number  num^2
num=2
print(f"square of number is {num**2}")
# Cube of number
# num^3
print(f"cube of number is {num**3}")

print("*************")

#Create a program taht takes two number as input and print whether the #first number is greater than,less than or equal to the second number

num1=int(input("Enter the num1: "))
num2=int(input("Enter the num2: "))
if num1>num2:
	print(f"{num1} is greater than {num2}")
elif num1<num2:
	print(f"{num1} is less than {num2}")
else:
	print(f"{num1} is equal to {num2}")