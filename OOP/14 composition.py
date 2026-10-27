class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()  # Created internally

    def start(self):
        self.engine.start()
        print("Car is ready to drive")


car = Car()
car.start()