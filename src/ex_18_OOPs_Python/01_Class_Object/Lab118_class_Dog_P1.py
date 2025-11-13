class Dog:
    # Attributes
    name = None
    breed = None
    height = None
    weight = None

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
        print("Bite")

print("Outsite of the class")
chow = Dog()
# chow - object_reference
# Dog() - object

rancho = Dog()
# rancho - object_reference
# Dog() - object