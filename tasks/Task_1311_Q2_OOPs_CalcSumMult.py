"""
You need to create a calculator function, but the calculator function has to take the value from the parameterized constructor.
So while creating the object, you will pass the parameters and that will basically return the sum of the two numbers, multiplication of two numbers.
"""

class CalcSumMult:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def mult(self):
        return self.a * self.b


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
calc = CalcSumMult(x, y)
print(f"Addition of {x} and {y} is: {calc.sum()}")
print(f"Multiplication of {x} and {y} is: {calc.mult()}")
