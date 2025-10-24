# Function to calculate normal pay
def normal_pay(hours, rate):
    return hours * rate

# Function to calculate overtime pay
def overtime_pay(overtime_hours, rate):
    return overtime_hours * rate

# Constants
normal_rate = 5
overtime_rate = 10
normal_hours = 40

# Input hours worked
hours_worked = int(input("Enter total hours worked: "))

# Calculate pay
if hours_worked > normal_hours:
    normal_hours_worked = normal_hours
    overtime_hours = hours_worked - normal_hours
    total_pay = normal_pay(normal_hours_worked, normal_rate) + overtime_pay(overtime_hours, overtime_rate)
else:
    total_pay = normal_pay(hours_worked, normal_rate)

print(f"Total Pay: ${total_pay}")
