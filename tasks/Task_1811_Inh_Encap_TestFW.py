"""
Task 18 Nov 2025 | Task Class Inheritance (SI) and Encapsulation
Build a Test Framework with Encapsulation + Inheritance
🎯 Goal:
Create a simple automation structure that uses:
A BaseTest class for setup/teardown (Parent class)
A LoginTest class that inherits BaseTest (Child class)
Encapsulate sensitive data (like credentials) as private variables
✅ Requirements:
Create a BaseTest class:
Has a protected variable _driver = "Chrome".
Method setup() prints "Launching browser: Chrome".
Method teardown() prints "Closing browser".
Create a LoginTest class that inherits BaseTest:
Has private variables for username and password.
Method run_test() that prints:
"Running login test with user: <username>".
Use encapsulation: access private vars only through a method (e.g., get_user()).
Create an object of LoginTest and call:
setup()
run_test()
teardown()
"""

class BaseTest:
    _driver = "Chrome"

    # def __init__(self, _driver):
    #     self._driver = _driver

    def setup(self):
        print(f"Launching browser: {self._driver}")

    def teardown(self):
        print("Closing browser")


class LoginTest(BaseTest):
    __username = "scott"
    __password = "tiger"

    def get_user(self):
        return self.__username

    def run_test(self):
        user = self.get_user()
        print(f"Running login test with user: {user}.")

lt = LoginTest()
lt.setup() # Launching browser: Chrome
lt.run_test() # Running login test with user: scott.
lt.teardown() # Closing browser