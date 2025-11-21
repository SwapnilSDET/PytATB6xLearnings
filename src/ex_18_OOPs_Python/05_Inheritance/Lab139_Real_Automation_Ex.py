class BaseTest:
    def __init__(self, browser):
        self.browser = browser

    def setup(self):
        print(f"Launching {self.browser}")

    def teardown(self):
        print(f"Tearing down {self.browser}")

class SignupTest(BaseTest):
    def run_test(self):
        self.setup()
        print("Running signup test...")
        self.teardown()


class LoginTest(BaseTest):
    def run_test(self):
        self.setup()
        print("Running login test...")
        self.teardown()

tsc = SignupTest("Chrome")
tsc.run_test()
# Launching Chrome
# Running signup test...
# Tearing down Chrome

tlc = LoginTest("Chrome")
tlc.run_test()
# Launching Chrome
# Running login test...
# Tearing down Chrome

tsf = SignupTest("Firefox")
tsf.run_test()
# Launching Firefox
# Running signup test...
# Tearing down Firefox

tlf = LoginTest("Firefox")
tlf.run_test()
# Launching Firefox
# Running login test...
# Tearing down Firefox


