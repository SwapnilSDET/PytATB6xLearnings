class TestExample:
    def __init__(self):
        self.driver = "Chrome"
        self._config = "Stage"
        self.__api__key = "ABC12345"

    def show(self):
        print(f"Driver: {self.driver}, Config: {self._config}, API Key: {self.__api__key}")

    def __private_method1(self):
        print("Private Method 1")

    def __private_method2(self):
        print("Private Method 2")

    def work(self):
        self.__private_method1()
        self.__private_method2()


obj = TestExample()
obj.show()
obj.work()

# Access levels:
# print(obj.driver)          # ✅ Public — accessible
# print(obj._config)         # ⚠️ Protected — accessible but discouraged
# print(obj.__api__key)     # ❌ Private — AttributeError