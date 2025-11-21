class TestSuite:
    def info(self):
        print("Test Suite Information")


class BaseTest(TestSuite):
    def setup(self):
        print("BaseTest setup")

    def run(self):
        print("BaseTest execution")

class LoginTest(BaseTest):
    def run(self):
        print("LoginTest execution")

class APITest(BaseTest):
    def run(self):  # overriding
        print("APITest execution")


test = LoginTest()  # LoginTest execution
# test = APITest()    # APITest execution
# test = BaseTest()   # BaseTest execution
test.run()          # Running method from the class for which instance is created
