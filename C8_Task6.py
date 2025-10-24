shopping_list = ["Milk", "Bread", "Eggs"]

shopping_list.append("Butter")
print(shopping_list)

shopping_list.extend(["Cheese", "Apples"])
print(shopping_list)

shopping_list.insert(2, "Juice")
print(shopping_list)

shopping_list.remove("Bread")
print(shopping_list)

shopping_list.pop(1)
print(shopping_list)

print(shopping_list.index("Eggs"))

print(shopping_list.count("Milk"))

shopping_list.sort()
print(shopping_list)

shopping_list.reverse()
print(shopping_list)