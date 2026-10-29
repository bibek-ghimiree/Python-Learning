try:
    a = 10
    b = 0
    print(a / b)

except ZeroDivisionError:
    print("You cannot divide by zero.")

try:
    age = int("hello")
    print(age)

except ValueError:
    print("Please enter a valid number.")

try:
    result = 10 + "20"
    print(result)

except TypeError:
    print("You cannot add an integer and a string directly.")
