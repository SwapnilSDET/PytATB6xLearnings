# Types of User defined functions
# 1. Non-returnable - does not return anything
# 2. Returnable - returns something
# 3. With parameters/arguments
# 4. without parameters/arguments

# ------------------------
# Builtin function
# ------------------------
import math

result = max(3, 4)
print(result)


# ------------------------
# User defined functions
# ------------------------

# 1. No return-type | No Arguments

def greet():
    print("Namaste...!")


greet()  # Namaste...!


# 2. No return-type | With Arguments

def greet_by_name(name):
    print("Namaste...!", name)


greet_by_name("Siyaa")  # Namaste...! Siyaa


# 3. No return-type | Default Arguments

def greet_with_default_args(name="Varsha"):
    print("Namaste...!", name.upper())


greet_with_default_args("Pradeep")  # Namaste...! PRADEEP
greet_with_default_args()  # Namaste...! VARSHA


# 4. No return-type | Default + Multiple Arguments
def greet_with_default_multiple_args(name1="Snehal", name2="Padekar"):
    print("Multiple Agrs => ", name1, name2)


greet_with_default_multiple_args()  # Multiple Agrs =>  Snehal Padekar
greet_with_default_multiple_args(name1="Samartha", name2="Padekar")  # Multiple Agrs =>  Samartha Padekar
greet_with_default_multiple_args(name2="Padekar", name1="Vaishnavi")  # Multiple Agrs =>  Vaishnavi Padekar
greet_with_default_multiple_args(name1="Vinay")  # Multiple Agrs =>  Vinay Padekar
greet_with_default_multiple_args(name2="Swapnil")  # Multiple Agrs =>  Snehal Swapnil


# 4. With return-type | with Arguments
def sum_of_two(a, b):
    return a + b


sum = sum_of_two(4, 6)
print(sum)


# 4. With return-type | with Default Arguments
def sum_of_two_def_args(num1=100, num2=200):
    print("The sum of 2 numbers are: ")
    return num1 + num2


result = sum_of_two_def_args(num1=100, num2=200)
print(result)
