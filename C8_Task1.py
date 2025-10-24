# Shopping List Program
# Initial shopping list
shopping_list = ["Banana", "Tomato", "Carrot", "Biscuits"]

print("Enter your shopping list:")
print(", ".join(shopping_list))

while True:
    new_item = input("Enter the new item (or type 'done' to finish): ")

    if new_item.lower() == "done":
        break

    shopping_list.append(new_item)

    print("\nYour new shopping list:")
    print(", ".join(shopping_list))
