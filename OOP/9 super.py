class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}")


class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def introduce(self):
        super().introduce()
        print(f"My grade is {self.grade}")


s = Student("Alice", 10)
s.introduce()