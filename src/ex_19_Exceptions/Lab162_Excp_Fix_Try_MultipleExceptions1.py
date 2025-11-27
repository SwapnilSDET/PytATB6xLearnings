try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a / b
    print(c)

except (TypeError, NameError, ValueError, ZeroDivisionError):
    print("Error Due to the Type,Name, Value or Zero Div!55")
