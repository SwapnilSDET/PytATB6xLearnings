# Here we can define as many exceptions as we can.

class InvalidAgeException(Exception):
    pass

# def check_zero_division(a):
#     if a < 0:
#         raise ZeroDivisionError("Can't divide by zero")

def can_you_drink(age):

    if age < 18:
        raise InvalidAgeException("Invalid age of drinking.")
    else:
        print("Enjoy your drinks.")

can_you_drink(25) # Enjoy your drinks.
# can_you_drink(17) # InvalidAgeException: Invalid age of drinking.
