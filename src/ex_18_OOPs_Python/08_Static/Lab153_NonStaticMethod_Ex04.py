class MathOperation:

    def div(self, a, b):
        return a / b

    @staticmethod
    def sum(a, b):
        return a + b

# To access non-static method we need to create an object of the class
t = MathOperation()
print(t.div(10, 10))

# We can access static method directly
print(MathOperation.sum(10, 10))