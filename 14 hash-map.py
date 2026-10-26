student = {
    "name": "Ram",
    "age": 20,
    "marks": 85
}

print(student["name"])
print(student.get("age"))

student["age"] = 21
student["grade"] = "A"

del student["marks"]

print(student)


student = {"name": "Ram", "age": 20, "marks": 85}

for key, value in student.items():
    print(key, value)

print(student.keys())
print(student.values())


numbers = [1, 2, 2, 3, 3, 3]
frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

print(frequency)
# {1: 1, 2: 2, 3: 3}