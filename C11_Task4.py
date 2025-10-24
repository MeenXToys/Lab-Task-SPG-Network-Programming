import re  # Import the regular expression module

# Sample input line containing an email
line = "From sales@shopmart.com sent at 09:45 AM"


# captures all characters after '@' until a space is found
# [^ ] means any character except space
# * means zero or more occurrences
# The parentheses () create a group, so only the part after '@' is returned
host = re.findall('@([^ ]*)', line)

# host is a list, so we take the first element host[0] to get the hostname
print(host)  # Output: shopmart.com
