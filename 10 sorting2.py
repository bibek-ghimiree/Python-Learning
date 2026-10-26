names = ["Ram", "Amit", "Sita", "Bina"]
names.sort()
print(names)

students = [
    ("Ram", 75),
    ("Sita", 95),
    ("Amit", 85)
]

students.sort(key=lambda student: student[1])
print(students)  # Sorted by marks