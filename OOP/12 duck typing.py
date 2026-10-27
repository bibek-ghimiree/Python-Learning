class Duck:
    def speak(self):
        print("Quack!")


class Person:
    def speak(self):
        print("Hello!")


class Robot:
    def speak(self):
        print("Beep!")


def make_it_speak(obj):
    obj.speak()


make_it_speak(Duck())
make_it_speak(Person())
make_it_speak(Robot())