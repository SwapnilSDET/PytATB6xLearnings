class VWOLoginPage:

    def __init__(self, email_agr, password_arg):
        self.email = email_agr
        self.password = password_arg

    def login_confirmation(self):
        if self.email == "sdetswapnil@sdetech.com" and self.password == "Sigm@2025":
            print("Access granted")
        else:
            print("Access denied")

email = input("Enter credentials for VWO Login - Email ID: ")
password = input("Enter credentials for VWO Login - Password: ")

vwo_objref = VWOLoginPage(email, password)
vwo_objref.login_confirmation()