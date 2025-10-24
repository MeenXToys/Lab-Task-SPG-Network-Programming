import re

print("Enter item lines (press Enter on an empty line to finish):")

lines = []
while True:
    line = input()
    if line.strip() == "":
        break
    lines.append(line)

# Extract prices from each line
prices = []
for line in lines:
    # Find numbers after the $ sign
    found = re.findall(r'\$([0-9.]+)', line)
    for price in found:
        prices.append(float(price))

# Calculate total
total = sum(prices)
print(f"Total: ${total:.2f}")
