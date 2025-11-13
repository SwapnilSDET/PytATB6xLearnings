# Variable concepts


a = 10 # This variable will be available throughout the program

class Person:
    b =11 # Instance/ Class Variable

    def print_info(self):
        c = 20 # Local variable
        print(c) # 20
        print(self.b) # 11
        print(a) # 10

obj_ref = Person()
obj_ref.print_info()
# print(b) - Not allowed
# print(c) - Not allowed