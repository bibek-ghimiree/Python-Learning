class Person:
    def __init__(self, age):
        self.age = age  # Calls the setter

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value


p = Person(20)

print(p.age)  # 20

p.age = 25
print(p.age)  # 25

# p.age = -5  # Raises ValueError


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


r = Rectangle(5, 4)

print(r.area)  # 20

r.width = 10
print(r.area)  # 40