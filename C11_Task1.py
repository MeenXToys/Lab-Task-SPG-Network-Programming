import re

# --- Using re.search ---
print("Using re.search():")
with open("system-log.txt", "r", encoding="utf-8") as fh:
    for line in fh:
        line = line.rstrip()
        if re.search(r"^Error:", line):
            print(line)

# --- Compare with startswith ---
print("\nUsing str.startswith():")
with open("system-log.txt", "r", encoding="utf-8") as fh:
    for line in fh:
        line = line.rstrip()
        if line.startswith("Error:"):
            print(line)
