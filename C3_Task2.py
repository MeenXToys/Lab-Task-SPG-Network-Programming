NORMAL_HOURS_LIMIT = 40
NORMAL_RATE = 5
OVERTIME_RATE = 10

# Get input from the user
try:
    hours = float(input("Enter Hours: "))
except ValueError:
    print("Invalid input. Please enter a number for hours.")
    exit()

# Initialize pay variable
pay = 0

# Check for overtime
if hours > NORMAL_HOURS_LIMIT:
    # 1. Calculate normal pay (first 40 hours)
    normal_pay = NORMAL_HOURS_LIMIT * NORMAL_RATE
    
    # 2. Calculate overtime hours and pay
    overtime_hours = hours - NORMAL_HOURS_LIMIT
    overtime_pay = overtime_hours * OVERTIME_RATE
    
    # 3. Calculate total pay
    pay = normal_pay + overtime_pay
else:
    # If no overtime, calculate pay at the normal rate
    pay = hours * NORMAL_RATE

print(f"Pay: {pay}")

# --- Output for the example 'Enter Hours: 45' ---
# Enter Hours: 45
# Pay: 250.0