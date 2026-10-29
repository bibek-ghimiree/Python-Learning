
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Result:", a / b)

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("The second number cannot be zero.")
