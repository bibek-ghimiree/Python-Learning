class Father:
    def skills(self):
        print("Gradening")

class Mother:
    def talent(self):
        print("Painting")

class Child(Mother,Father):
    def hobbies(self):
        print("Child: PLaying football")

C = Child()

C.talent()
C.hobbies()
C.skills()