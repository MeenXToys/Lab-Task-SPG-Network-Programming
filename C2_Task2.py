import time

# Prompt the user for input
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

# Calculate gross pay
pay = hours * rate

# Pause for 1 second before showing the result
time.sleep(1)

# Display the result
print("Pay:", pay)
