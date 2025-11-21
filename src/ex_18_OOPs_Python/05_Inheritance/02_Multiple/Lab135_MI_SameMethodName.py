# Multiple Inheritance: A class inherits from more than one parent class.
# Multiple Parents -> Single Child ==>> This is not allowed in Java.
# What is MRO (Method Resolution Order) in Python?**
# MRO stands for Method Resolution Order.
# It is the order in which Python searches for a method or attribute when multiple inheritance is used.
# It defines which parent class method is called first.

class Father1:

    def money(self): # Same Method name in both the parent classes
        print("Father 1 Money")

class Father2:

    def money(self): # Same Method name in both the parent classes
        print("Father 2 Money")

class Child(Father1, Father2):
    def give_money(self):
        print("Child class")
        self.money() # The method is called from the parent class method is called first


c = Child()
c.give_money()
