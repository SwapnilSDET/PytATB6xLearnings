class MathClass:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c=10):
        return a + b + c


obj_ref = MathClass()
print(obj_ref.add(100, 200, 300))
print(obj_ref.add(3.14, 6.28)) # Here, the value of c will be added by-default

# In case of method overloading,
# when a function is available with same name but with additional parameters
# - then the function with max parameters will be used.
