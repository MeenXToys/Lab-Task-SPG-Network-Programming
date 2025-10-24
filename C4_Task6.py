# Define the function with default parameter
def show_employee(name, salary=9000):
    # Display employee name and salary
    print("Employee Name:", name)
    print("Salary:", salary)

# Call the function with both name and salary
show_employee("Alice", 12000)

# Call the function with only name (salary will use default value 9000)
show_employee("Bob")
