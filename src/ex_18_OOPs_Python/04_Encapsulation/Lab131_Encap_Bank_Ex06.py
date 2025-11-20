class Bank:
    def __init__(self, acc_no, bal):
        self.__acc_no = acc_no  # Private
        self.balance = bal  # Public

    def check_balance(self):
        print(self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount

    def show_me_the_acc_no(self, is_auth):
        if is_auth == True:
            print(self.__acc_no)
        else:
            print("You are not authorized.")

icici = Bank(9876543210, 100)
icici.deposit(100)
icici.check_balance()
# print(icici.__acc_no) - will give error - AttributeError: 'Bank' object has no attribute '__acc_no'
print(icici.show_me_the_acc_no(True)) # If you are a cashier then only you can see the acc_no because of the encapsulation