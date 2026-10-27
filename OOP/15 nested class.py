class University:

    class Department:
        def __init__(self, name):
            self.name = name

        def show(self):
            print(f"Department: {self.name}")


dept = University.Department("Computer Science")
dept.show()

class Computer:
    def __init__(self, brand):
        self.brand = brand
        self.cpu = self.CPU("Intel")

    def show(self):
        print(self.brand)
        print(self.cpu.name)

    class CPU:
        def __init__(self, name):
            self.name = name


pc = Computer("Dell")
pc.show()