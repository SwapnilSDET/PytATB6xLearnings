# Problem to find the max between two.

# Logic Building Formula

# 1. I/O -> user inputs -> two integers
# 2. O/P -> int 1 which ever is greater, return it using max number.
# 31.4 or 45.34 - float

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

# if num1 > 0 and num2 > 0:
#     print("Number should be positive")

if num1 >= num2: # num1 == num2 ->  Handled.
    print("Max of 2 numbers is: ", num1)
else:
    print("Max of 2 numbers is: ", num2)