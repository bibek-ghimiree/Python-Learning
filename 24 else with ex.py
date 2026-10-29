

try:
    a = int(input("Enter a number: "))
    result = 100 / a

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Invalid input.")

else:
    print("Result:", result)

