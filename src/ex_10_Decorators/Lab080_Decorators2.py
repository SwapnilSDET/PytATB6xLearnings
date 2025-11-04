def before_after_ui_tc(func):
    def wrapper():
        print("Before running UI TC") # before
        func() # func_call
        print("After running UI TC") # after
    return wrapper()

@before_after_ui_tc
def test_ui():
    print("I am testing a UI test case.")