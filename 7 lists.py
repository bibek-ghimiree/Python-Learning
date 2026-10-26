fruits = ["apple", "banana", "mango"]

print(fruits[0])     # apple
print(fruits[-1])    # mango
print(len(fruits))   # 3

fruits.append("orange")
fruits.insert(1, "grape")
fruits.remove("banana")

last = fruits.pop()
print(fruits)
print(last)

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])  # [20, 30, 40]
print(30 in numbers) # True

numbers[0] = 100
numbers.sort()
numbers.reverse()

print(numbers)