# python 3.11 & above

# Here, we can create a group and use as per our requirements
# In case of custom exceptions, you don't need to follow try-except-else-finally. Just raise the exception.

eg = ExceptionGroup("Mutliple Exceptions", [
    ValueError("Invalid Value"),
    TypeError("Invalid Type"),
    ZeroDivisionError("Incorrect divison"),
])

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def check_div(a,b):
    if a == 0 or b == 0:
        raise eg