# To hide sensitive information from the code (like credentials) - the .env file is used.
# Created a .env file
# In terminal run - pip install dotenv
# We will not push .env file to github as it contains confidential data

from dotenv import load_dotenv # Created by Python community
import os # os - Operating System # Created by Python creators

class VWOLoginPage:

    def __init__(self, email_agr, password_arg):
        self.email = email_agr
        self.password = password_arg

    def login_confirmation(self):

        load_dotenv() # This function loads the .env file

        # os.getenv() - This function fetched the corresponding values from the file
        if self.email == os.getenv("USERNAME") and self.password == os.getenv("PASSWORD"):
            print("Access granted")
        else:
            print("Access denied")

email = input("Enter credentials for VWO Login - Email ID: ")
password = input("Enter credentials for VWO Login - Password: ")

vwo_objref = VWOLoginPage(email, password)
vwo_objref.login_confirmation()

print(os.name) # nt for Windows, posix for Mac