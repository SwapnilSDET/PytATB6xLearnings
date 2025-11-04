def decorator1(func):
    def wrapper():
        print("Decorator1 - Before function")
        func()
        print("Decorator1 - After function")
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator2 - Before function")
        func()
        print("Decorator2 - After function")
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello World")

say_hello()