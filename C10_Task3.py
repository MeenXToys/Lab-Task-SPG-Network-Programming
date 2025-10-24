# Create a dictionary with the data
courses = {
    'SPG': 1,
    'COS': 2,
    'IEP': 3,
    'MPU': 4
}

# Use sorted() to sort the dictionary by keys
for key, value in sorted(courses.items()):
    print(key, value)

