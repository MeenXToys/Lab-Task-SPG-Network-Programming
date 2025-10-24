# Define the function with variable length arguments
def func1(*args):
    print("Printing values:")
    for value in args:
        print(value)

# Call the function
func1(20, 60, 30)
