Here’s a Python program to find the largest of three numbers:

Copy the code
# Program to find the largest of three numbers

# Input three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Determine the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Output the result
print(f"The largest number is: {largest}")


This program uses conditional statements to compare the three numbers and determine the largest one. It’s simple, efficient, and easy to understand!