people = 30
cars = 40
buses = 15

# Decision for cars
if cars > people:
    print("We should take cars")
elif cars < people:
    print("We should not take the cars")
else:
    print("We can't decide")

# Decision for buses vs cars
if buses > cars:
    print("That's too many buses")
elif buses < cars:
    print("Maybe we could take the buses")
else:
    print("We still can't decide")

# Final decision: buses vs people
if buses > people:
    print("Alright, let's just take the buses")
else:
    print("Fine, let's stay home then")