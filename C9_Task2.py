Type = {
    'A': 'Ultraman',
    'B': 'Power Rangers',
    'C': 'Masked Rider',
    'D': 'Power Puff Girl'
}


print("What character would you like to be?")
print("Type A for Ultraman")
print("Type B for Power Rangers")
print("Type C for Masked Rider")
print("Type D for Power Puff Girl")


choice = input("Choice: ").upper()


if choice in Type:
    print("You've selected", Type[choice])
else:
    print("Invalid choice! Please select A, B, C, or D.")
