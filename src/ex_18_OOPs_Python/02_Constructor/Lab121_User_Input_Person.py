class Person:
    # name = None
    # age = None
    # phone = None
    # occupation = None

    def __init__(self):
        print("Please enter the name, age, phone, occupation: ")
        self.name = input("Enter the name: ")
        self.age = input("Enter the age: ")
        self.phone = input("Enter the phone: ")
        self.occupation = input("Enter the occupation: ")

    def display_info(self):
        print("You have entered the following information => ")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Phone:", self.phone)
        print("Occupation:", self.occupation)

ob_ref = Person()
ob_ref.display_info()
