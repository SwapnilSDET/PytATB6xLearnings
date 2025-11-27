a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

try:
    c = a / b
    print(c)

except ZeroDivisionError:
    print("The division by zero is not allowed.")
