class Animal:
    def eat(self):
        print("this animal eats food")

class Dog(Animal):
    def barks(self):
        print("Woof!");


dog = Dog()

dog.eat();
dog.barks();