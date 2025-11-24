"""
Create a Person class where we will have five attributes and five behaviors.
Make sure that each type of function is used,
and I want you to also create the print function,
which will print all the instance variable values.
"""

class Person:
    def __init__(self, name, age, email, contact, occupation):
        self.p_name = name
        self.p_age = age
        self.p_email = email
        self.p_contact = contact
        self.p_occupation = occupation

    def printDetails(self):
        print("Name:", self.p_name)
        print("Age:", self.p_age)
        print("Email:", self.p_email)
        print("Contact:", self.p_contact)
        print("Occupation:", self.p_occupation)

    def read(self):
        print(self.p_name, "can read 5 different languages.")

    def display_age(self):
        print(f"{self.p_name} is {self.p_age} years old.")

    def regEmail(self):
        print(f"{self.p_name} has a registered email id as - {self.p_email}")

    def showContact(self):
        print(f"{self.p_name} has a contact number as - {self.p_contact}")

    def showOccupation(self):
        print(f"{self.p_name} is a {self.p_occupation}")

swapnil = Person("Swapnil", "38", "9876543210", "swapnil@yopmail.com", "Software Engineer")
swapnil.printDetails()

swapnil.read()
swapnil.display_age()
swapnil.regEmail()
swapnil.showContact()
swapnil.showOccupation()
