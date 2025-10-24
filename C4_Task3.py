def calculate_area(length, width):
    area = length * width
    return area

i = float(input("Enter the length of the rectangle: "))
w = float(input("Enter the width of the rectangle: "))

result = calculate_area(i, w)
print("The area of the rectangle is:", result)
