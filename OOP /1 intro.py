class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
    def drive(self):
        print(f"{self.brand} is driving")

    def showInfo(self):
        print(f"Brand: {self.brand}, Color: {self.color}");

car1 = Car("BMW", "Black")

car1.showInfo();
car1.drive();
