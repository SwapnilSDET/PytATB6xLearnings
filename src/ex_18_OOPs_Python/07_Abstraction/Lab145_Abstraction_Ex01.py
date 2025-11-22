# Abstraction
# Hide the details & show the required part

# Car -> with key _ __private, tyres -> public
# Car -> multiple - Engine, GearBox
# Car -> driver -> Engine, gearbox?

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Barking")

dog = Dog("Browniee")
dog.sound()