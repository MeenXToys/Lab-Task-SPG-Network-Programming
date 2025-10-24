import re

text = input("Enter a sentence with numbers: ")
numbers = re.findall(r"[0-9]+", text)
print(numbers)
