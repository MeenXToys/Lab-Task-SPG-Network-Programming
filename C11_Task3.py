import re

# Ask user to enter a sentence with email addresses
text = input("Enter a sentence with email addresses: ")

# Use regex to find all emails in the input
emails = re.findall(r'\S+@\S+', text)

# Print the list of emails found
print("Extracted emails:", emails)
