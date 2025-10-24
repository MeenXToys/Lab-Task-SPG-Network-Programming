# Ask the user to input two band names for the first tuple
band1_name1 = input("Enter the first band for tuple 1: ")
band1_name2 = input("Enter the second band for tuple 1: ")

# Ask the user to input two band names for the second tuple
band2_name1 = input("Enter the first band for tuple 2: ")
band2_name2 = input("Enter the second band for tuple 2: ")

# Create tuples
band1 = (band1_name1, band1_name2)
band2 = (band2_name1, band2_name2)

# Compare tuples
result = band1 < band2

# Display result
print("\nTuple 1:", band1)
print("Tuple 2:", band2)
print("Comparison result (Tuple 1 < Tuple 2):", result)
