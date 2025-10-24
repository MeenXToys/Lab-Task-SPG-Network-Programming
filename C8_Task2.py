# Program to insert a word in the middle of a sentence

# Initial sentence as a list
sentence = ["Saya", "NWS2"]
print(sentence)

# Ask user for a word
word = input("Enter a word: ")

# Insert the word in the middle (index 1)
sentence.insert(1, word)

# Display new list
print(sentence)
