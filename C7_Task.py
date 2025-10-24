# 1. Open the file in write mode and write some data
file = open("C7_Task.txt", "w")
file.write("Hello, this is a file handling task.\n")
file.write("We are learning open, write, read, seek, and tell.")
file.close()  # always close the file

# 2. Open the file in read mode and read content
file = open("C7_Task.txt", "r")
print("File Content:\n")
print(file.read())  # read the whole content

# 3. Use seek() to move the file pointer to a specific position
file.seek(7)  # Move to the 7th byte in the file
print("\nPointer moved to position 7")

# 4. Use tell() to display current pointer position
position = file.tell()
print("Current pointer position:", position)

# 5. Read from the new position
print("Reading after seek():", file.read(10))

file.close()
