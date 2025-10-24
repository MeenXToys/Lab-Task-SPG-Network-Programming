# Demonstrating Python list methods

# Initial list
my_list = ["Apple", "Banana", "Orange"]
print("Initial list:", my_list)

# 1. append(x) → Adds item at the end
my_list.append("Grapes")
print("After append('Grapes'):", my_list)

# 2. extend(L) → Adds another list
my_list.extend(["Mango", "Papaya"])
print("After extend(['Mango', 'Papaya']):", my_list)

# 3. insert(i, x) → Inserts at position 1
my_list.insert(1, "Kiwi")
print("After insert(1, 'Kiwi'):", my_list)

# 4. remove(x) → Removes first occurrence of "Banana"
my_list.remove("Banana")
print("After remove('Banana'):", my_list)

# 5. pop(i) → Removes and returns element at index 2
removed_item = my_list.pop(2)
print("After pop(2):", my_list, " (Removed:", removed_item, ")")

# 6. index(x) → Find index of "Mango"
index_mango = my_list.index("Mango")
print("Index of 'Mango':", index_mango)

# 7. count(x) → Count how many times "Apple" appears
apple_count = my_list.count("Apple")
print("Count of 'Apple':", apple_count)

# 8. sort() → Sort list alphabetically
my_list.sort()
print("After sort():", my_list)

# 9. reverse() → Reverse list order
my_list.reverse()
print("After reverse():", my_list)
