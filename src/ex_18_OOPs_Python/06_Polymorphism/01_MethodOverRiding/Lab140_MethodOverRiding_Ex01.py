class BaseTest:
    def run(self):
        print("Running BaseTest")

class LoginTest(BaseTest):
    def run(self):
        print("Running LoginTest")

test = LoginTest()
test.run() # Running LoginTest - bcz the object is created for LoginTest()
