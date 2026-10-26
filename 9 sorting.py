numbers = [5, 2, 9, 1, 7]

# Create a sorted copy
result = sorted(numbers)
print(result)
print(numbers)
# Sort the original list
numbers.sort()
print(numbers)

# Descending order
numbers.sort(reverse=True)
print(numbers)