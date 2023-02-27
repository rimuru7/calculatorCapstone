# V-1.0
# Done By Rushi, Mohan, Dhanunjay
import sys

# Define the basic math operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Get user input for numbers and operation
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the math operation (+, -, *, /): ")
except ValueError:
    print("Invalid input!")
    sys.exit()

# Perform the operation based on user input
if operation == "+":
    print("Result: ", add(num1, num2))
elif operation == "-":
    print("Result: ", subtract(num1, num2))
elif operation == "*":
    print("Result: ", multiply(num1, num2))
elif operation == "/":
    if num2 == 0:
        print("Error: Division by zero!")
        sys.exit()
    else:
        print("Result: ", divide(num1, num2))
else:
    print("Invalid operation!")


