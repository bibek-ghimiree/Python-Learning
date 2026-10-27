class Teacher:
    def __init__(self, name):
        self.name = name


class Department:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher  # Existing object is supplied

    def show(self):
        print(
            f"{self.teacher.name} teaches in {self.name}"
        )


teacher1 = Teacher("Mr. Smith")
department1 = Department("Science", teacher1)

department1.show()

del department1
print(teacher1.name)  # Mr. Smith