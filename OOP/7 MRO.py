class A:
    def show(self):
        print("Class A")


class B:
    def show(self):
        print("Class B")


class C(A, B):
    pass


obj = C()
obj.show()         # Class A
print(C.mro())     # Shows the lookup order
obj.show()