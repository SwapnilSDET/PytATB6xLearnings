# MultiLevel ==>> GrandFather -> Father -> Child


class TestSuite:
    def info(self):
        print("Grandfather -> TestSuite - Step 1")

class BaseTest(TestSuite):
    def setup(self):
        print("Father -> BaseTest - Step 2")

class UITest(BaseTest):
    def run(self):
        self.info()     # Grandfather -> TestSuite - Step 1
        self.setup()    # Father -> BaseTest - Step 2
        print("Child -> UITest - Step 3")   # Child -> UITest - Step 3

test = UITest()
test.run()