# Create a dictionary with month names and numbers
months = {
    'August': 8,
    'January': 1,
    'March': 3
}

# Create an empty list to store tuples
tmp = []

# Loop through dictionary and flip key-value to value-key
for key, value in months.items():
    tmp.append((value, key))

# Sort the list in ascending order by value
tmp.sort()
print("Ascending order:", tmp)

# Sort the list in descending order by value
tmp.sort(reverse=True)
print("Descending order:", tmp)



