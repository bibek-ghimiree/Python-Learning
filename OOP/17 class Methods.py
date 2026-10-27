class Student:
    school = "ABC College"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    @classmethod
    def from_string(cls, text):
        name = text.split("-")[0]
        return cls(name)


s1 = Student("Alice")
Student.change_school("XYZ College")

print(s1.school)

s2 = Student.from_string("Bob-Grade10")
print(s2.name)


class Demo:
    value = 100

    def instance_method(self):
        return self.value

    @classmethod
    def class_method(cls):
        return cls.value

    @staticmethod
    def static_method(a, b):
        return a + b


d = Demo()

print(d.instance_method())      # 100
print(Demo.class_method())      # 100
print(Demo.static_method(2, 3)) # 5