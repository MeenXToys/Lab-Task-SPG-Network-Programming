# Define the function
def calculation(a, b):
    add = a + b
    sub = a - b
    return add, sub   # returning both values together

# Get input from user
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

# Call the function
result = calculation(x, y)

# Unpack the returned values
addition, subtraction = result

# Display results
print("Addition:", addition)
print("Subtraction:", subtraction)
