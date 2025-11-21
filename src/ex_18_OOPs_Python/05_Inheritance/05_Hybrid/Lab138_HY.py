# Hybrid Inheritance
# This is a mixture of all types of inheritance.

class Base:
    def base_method(self):
        print("Inside Base method.")

class A(Base): # Hierarchical
    def a_method(self):
        print("Inside A method.")

class B(Base): # Hierarchical
    def b_method(self):
        print("Inside B method.")

class C(A, B): # Multiple
    def c_method(self):
        print("Inside C.")


obj = C()
obj.base_method()
obj.a_method()
obj.b_method()
obj.c_method()