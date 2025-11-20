class Home:
    def __init__(self):
        self.public_var = "Father"
        self._protected_var = "Brother"
        self.__private__var = "Baby"

    def mother(self):
        print("Mother - This is a Public function.")
        print(self.__private__var)
        self.__wife()

    def __wife(self):
        print("Wife - This is a PRIVATE function.")

obj_ref = Home()
# obj_ref.__wife() - Outside of the class - Not allowed
# obj_ref.__private__var - Outside of the class - Not allowed

obj_ref.mother() # This is a public function can access PRIVATE variables (within the class) - called encapsulation.

# print(object_ref._protected_var)
# ⚠️ Technically accessible, but not recommended