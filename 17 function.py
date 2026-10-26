def greet():
    print("Hello!")

greet()

def add(a, b):
    return a + b

result = add(10, 20)
print(result)


def greet(name, message="Welcome"):
    print(f"{message}, {name}!")

greet("Ram")
greet("Sita", message="Hello")

def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3, 4, 5))