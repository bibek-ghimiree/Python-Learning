# nested functions
def outer():
    message = "Hello"

    def inner():
        print(message)

    inner()

outer()


def multiplier(factor):
    def multiply(number):
        return number * factor

    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15


def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

next_count = counter()

print(next_count())  # 1
print(next_count())  # 2
print(next_count())  # 3