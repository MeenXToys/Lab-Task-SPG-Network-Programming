word = input("Enter a word: ")

if word == "banana":
    print("All right, bananas.")
elif word < "banana":
    print("Your word, " + word + ", comes before banana.")
else:
    print("Your word, " + word + ", comes after banana.")
