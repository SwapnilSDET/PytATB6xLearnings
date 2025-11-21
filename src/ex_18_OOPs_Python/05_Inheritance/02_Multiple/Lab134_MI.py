# Multiple Inheritance: A class inherits from more than one parent class.
# Multiple Parents -> Single Child
# This is not allowed in Java.


class APIBase:

    def api_auth(self):
        print("Authenticating API...")

class DBBase:

    def db_auth(self):
        print("Authenticating DB...")

class TestHybrid(APIBase, DBBase):
    def run(self):
        print("Testing Hybrid with 2 base classes - Yes, it's possible in Python.")
        self.api_auth()
        self.db_auth()

tc1 = TestHybrid()
tc1.run()

