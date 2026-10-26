numbers = {1, 2, 3, 3, 4}
print(numbers)  # Duplicate 3 is removed

numbers.add(5)
numbers.remove(2)
numbers.discard(10)  # No error if missing

print(3 in numbers)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)  # Union
print(a & b)  # Intersection
print(a - b)  # Difference
print(a ^ b)  # Symmetric difference