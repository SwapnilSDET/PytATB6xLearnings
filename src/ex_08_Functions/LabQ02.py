# Nested functions are allowed but internal function should be called first

def f1():
    print("Welcome")
    #Step 1- Declare
    def f2():
        print("Hi")

    #Step 2 - Call
    f2()


f1()
# f2()