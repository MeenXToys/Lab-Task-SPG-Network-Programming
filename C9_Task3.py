names = ['Raphael', 'Donatello', 'Michelangelo', 'Leonardo']
numbers = [103, 104, 102, 101]

# Display the lists
print(names)
print(numbers)

# Combine them using zip()
combined = list(zip(names, numbers))
print(combined)

# Convert to dictionary
dictionary = dict(zip(names, numbers))
print(dictionary)

