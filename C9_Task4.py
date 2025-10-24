sentence = "If you love something, let it go. If it comes back, it was meant to be. If it does not, hunt it down and kill it"

# Convert sentence to lowercase and split into words
words = sentence.lower().replace('.', '').replace(',', '').split()

#word = ['if','you','love','something','let','it','go','if', ...]

# Create an empty dictionary to count words
word_count = {}

# Count occurrences
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
                        #Set the dictionary entry for word to the previous count plus 1.

# Display results
for word, count in word_count.items():
    print(f"{word}: {count}")

#.items() returns all key-value pairs from the dictionary.

