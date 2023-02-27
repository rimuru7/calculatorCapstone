import math

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

# Function to get the modulus of two numbers
def modulus(x, y):
    return x % y

# Function to get the power of a number
def power(x, y):
    return x ** y

# Function to get the sine of a number
def sine(x):
    return math.sin(math.radians(x))

# Function to get the cosine of a number
def cosine(x):
    return math.cos(math.radians(x))

# Function to get the tangent of a number
def tangent(x):
    return math.tan(math.radians(x))

# Function to get the arc sine of a number
def arcsine(x):
    return math.degrees(math.asin(x))

# Function to get the arc cosine of a number
def arccosine(x):
    return math.degrees(math.acos(x))

# Function to get the arc tangent of a number
def arctangent(x):
    return math.degrees(math.atan(x))

# Main function to take input from user and perform calculations
def main():
    print("Welcome to the Trigonometric Calculator Program in Python")

    while True:
        print("Please select the operation you want to perform: ")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Sine")
        print("8. Cosine")
        print("9. Tangent")
        print("10. Arc Sine")
        print("11. Arc Cosine")
        print("12. Arc Tangent")
        print("13. Exit")

        choice = input("Enter choice (1/2/3/4/5/6/7/8/9/10/11/12/13): ")