try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a / b

except TypeError:
    print("TypeError")
except NameError:
    print("NameError")
except ValueError:
    print("ValueError")
except ZeroDivisionError:
    print("ZeroDivisionError")

else: # Runs only if try block succeeds.
    print(f"{a} divided by {b} is equal to {c}.")

finally:
    print("Finally statement always executed.")