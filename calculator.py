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

# Main function to take input from user and perform calculations
def main():
    print("Welcome to the Basic Calculator Program in Python")

    while True:
        print("Please select the operation you want to perform: ")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        choice = input("Enter choice (1/2/3/4/5/6/7): ")

        if choice == '7':
            break

        try:
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

            else:
                print("Invalid input, please enter a valid choice.")

        except ValueError as e:
            print("Invalid input, please enter a valid number. Error message: ", str(e))

if __name__ == '__main__':
    main()