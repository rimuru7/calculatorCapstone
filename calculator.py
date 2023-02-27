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