# Initial values (same as before)
people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats. The world is doomed")
elif people > cats:
    print("Not many cats. The world is saved")
elif people < dogs:
    print("The world is drooled on!")
elif people > dogs:
    print("The world is dry!")
else:
    # This only happens if people == cats AND people == dogs
    pass # No output specified for this case