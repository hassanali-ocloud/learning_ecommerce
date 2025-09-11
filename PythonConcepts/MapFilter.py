a = ["1a", 2, 3]
b = ["4a", 5, 6]
summed = list(map(lambda x, y: x + y, a, b))
print("Summed:", summed)

words = ["apple", "banana", "cherry", "date"]
long_words = list(filter(lambda w: len(w) > 5, words))
print("Long words:", long_words)