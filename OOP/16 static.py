class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(number):
        return number % 2 == 0


print(Calculator.add(10, 20))
print(Calculator.is_even(8))
print(Calculator.is_even(7))