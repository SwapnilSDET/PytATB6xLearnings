# Problem  Find the Max between 3 numbers

# Logic Building

# I/P -> User inputs - num1, num2, num3 -> int
# O/P -> int or String with max number.

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

if num1 >= num2 and num1 >= num3:
    print("Max of 3 numbers is: ", num1)
elif num2 >= num1 and num2 >= num3:
    print("Max of 3 numbers is: ", num2)
else:
    print("Max of 3 numbers is: ", num3)