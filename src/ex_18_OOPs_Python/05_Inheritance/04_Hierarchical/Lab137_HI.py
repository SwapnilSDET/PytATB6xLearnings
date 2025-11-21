# Hierarchical ==>> One Father => Multiple Childs

class BaseTest:
    def setup(self):
        print("Setting up in BaseTest")

class SignupTest(BaseTest):
    def run(self):
        print("Running - SignupTest from BaseTest")

class SigninTest(BaseTest):
    def run(self):
        print("Running - SigninTest from BaseTest")

SignupTest().setup()    # Setting up in BaseTest
SignupTest().run()      # Running - SignupTest from BaseTest

SigninTest().setup()    # Setting up in BaseTest
SigninTest().run()      # Running - SigninTest from BaseTest
