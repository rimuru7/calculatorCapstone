# Version 3.0 
# Done By: Rushi, Mohan, Dhanunjay
# Trigonometric Calculator Program in Python

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
def logarithm(x):
    return math.log(x)

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
        print("10. Arc Sine ")
        print("11. Arc Cosine")
        print("12. Arc Tangent")
        print("13. Natural Logarithm")
        print("14. Exit")
        

        choice = input("Enter choice (1/2/3/4/5/6/7/8/9/10/11/12/13/14): ")

        if choice == '14':
            break

        try:
            if choice in ['7', '8', '9', '10', '11', '12','13']:
                num = float(input("Enter number: "))
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result: ", add(num1, num2))

            elif choice == '2':
                print("Result: ", subtract(num1, num2))

            elif choice == '3':
                print("Result: ", multiply(num1, num2))

            elif choice == '4':
                print("Result: ", divide(num1, num2))

            elif choice == '5':
                print("Result: ", modulus(num1, num2))

            elif choice == '6':
                print("Result: ", power(num1, num2))

            elif choice == '7':
                print("Result: ", sine(num))

            elif choice == '8':
                print("Result: ", cosine(num))

            elif choice == '9':
                print("Result: ", tangent(num))

            elif choice == '10':
                print("Result: ", arcsine(num))

            elif choice == '11':
                print
            elif choice == '12':
                print("Result: ", arctangent(num))

            else:
                print("Invalid input, please try again")

        except ValueError as e:
            print("Error:", e)
            continue


if __name__ == '__main__':
    main()

