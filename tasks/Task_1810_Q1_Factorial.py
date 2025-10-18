"""
Given a Number a number you need to calculate the factorial of that number
n = 5
Fact = 5×4×3*2*1 = 120
Fact = 0 → 1,
"""

# Take the input from user
n = int(input("Enter a number: "))
fact = 1

if n < 0:
    print(f"The number {n} is negative. Factorial does not exist for negative numbers.")
elif n == 0:
    print(f"The number {n} is zero. The factorial of 0 is always 1")
else:
    for i in range(1,n+1):
        fact = fact * i
    print(f"The factorial of {n} is {fact}")