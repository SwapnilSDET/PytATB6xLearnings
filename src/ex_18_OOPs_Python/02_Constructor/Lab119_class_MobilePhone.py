print("Outsite of the class1")


class MobilePhone:
    model = None

    def __init__(self):
        print("This is a DC - Default Constructor")

    def talk(self):
        print("I am talking")

iPhone = MobilePhone() # This is a DC - Default Constructor
iPhone.talk() # I am talking

print("Outsite of the class2")

