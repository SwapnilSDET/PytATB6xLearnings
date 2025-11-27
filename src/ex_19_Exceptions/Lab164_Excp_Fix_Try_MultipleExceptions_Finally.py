try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a / b
    print(c)

except TypeError:
    print("TypeError")
except NameError:
    print("NameError")
except ValueError:
    print("ValueError")
except ZeroDivisionError:
    print("ZeroDivisionError")

finally:
    print("Finally statement always executed.")