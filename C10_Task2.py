GMI = ('NWS', 'PIC', 'MEC', 'EIT')

print("Available courses:")
print("0 -", GMI[0])
print("1 -", GMI[1])
print("2 -", GMI[2])
print("3 -", GMI[3])

while True:
    choice = input("Choose your course number (0-3): ")

    # Check if input is a number
    if choice.isdigit():
        choice = int(choice)
        # Check if number is in valid range
        if 0 <= choice <= 3:
            print("I choose", GMI[choice], "as my main course in GMI")
            break  # exit the loop once valid input is given
        else:
            print("Error: Please enter a number between 0 and 3.")
    else:
        print("Error: Please enter numbers only (0-3).")
