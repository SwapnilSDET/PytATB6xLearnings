"""
Q1 - Create a function which will take a positive number from the user and perform square of the number?
i/o = 3 | o/p = 9
"""

def sqrOfNum(num):
    if num == 0:
        return 0
    else:
        return num ** 2

num = int(input("Enter a number: "))
print("Square of the number is: ", sqrOfNum(num))