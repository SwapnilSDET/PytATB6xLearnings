# Encapsulation -
# Hide the data members(class variables, instance variables) by using only the methods.

class Car:

    def __init__(self):
        self.public_me = "This is public me." # Public variable can be accessed from anywhere
        self.__private_baby = "This is my private baby." # Private variable can be accessed only within the class

    def nany(self): # This function is used to access private variable
        self.__private_baby = "This is my private baby."
        return self.__private_baby


obj_ref = Car()
print(obj_ref.public_me)
print(obj_ref.nany())


# print(obj_ref.__private_var)
# This will give error
# Output -
# Traceback (most recent call last):
#   File "C:\Users\SP\PycharmProjects\PytATB6xLearnings\src\ex_18_OOPs_Python\04_Encapsulation\Lab130_Encap_Ex05.py", line 13, in <module>
#     print(obj_ref.__private_var)
#           ^^^^^^^^^^^^^^^^^^^^^
# AttributeError: 'Car' object has no attribute '__private_var'. Did you mean: '_Car__private_var'?
