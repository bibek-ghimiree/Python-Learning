
age = 15

if age < 18:
    raise ValueError("Age must be at least 18")

print("Access granted")
try:
    age = 15

    if age < 18:
        raise ValueError("Age must be at least 18")

except ValueError as e:
    print("Error:", e)

