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
