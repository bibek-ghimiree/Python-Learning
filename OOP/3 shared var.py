class Employee:
    company = "Tech Corp"
    employee_count = 0

    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1


e1 = Employee("Sam")
e2 = Employee("Mia")

print(Employee.employee_count)  # 2