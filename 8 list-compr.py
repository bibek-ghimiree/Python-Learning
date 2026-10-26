squares = []

for i in range(1, 6):
    squares.append(i ** 2)

print(squares)

squares = [i ** 2 for i in range(1, 6)]
print(squares)

even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(even_numbers)

words = ["apple", "cat", "banana", "dog"]
long_words = [word for word in words if len(word) > 3]
print(long_words)