class Stud:
    school = "Himalayan School" # Class variable

    def __init__(self,name,grade):
        # Instance variable
        self.name = name
        self.grade = grade


s1 = Stud("Alina","90")
print(s1.name)
print(s1.grade)
print(s1.school)

Stud.school = "Himalayan Public School"

print(s1.school)