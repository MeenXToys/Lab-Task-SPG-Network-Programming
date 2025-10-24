# Define functions
def add(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# Get input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform operations
print("Addition:", add(num1, num2))
print("Subtraction:", minus(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))
