class Dog:
    # Attributes - Instance/Data/Class Variables
    name = None
    breed = None
    height = None
    weight = None

    # Default + Parameterized constructor
    def __init__(self, given_name, given_breed, given_height, given_weight):
        self.name = given_name
        self.breed = given_breed
        self.height = given_height
        self.weight = given_weight

    # behaviour
    def bark(self):
        print("Barking")
        # print(name)
        print(self.name)

    def run(self):
        print("Running")

    def smell(self):
        print("Smelling")

    def bite(self):
        print(self.name, "Bite")


chow = Dog("Chow", "Breed1", "Height1", "Weight1")
Rancho = Dog("Rancho", "Breed2", "Height2", "Weight2")

chow.bite()
Rancho.bite()

