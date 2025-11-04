"""
Checking for a leap year, 2024 -> Yes
Multiple of 400
Multiple of 4 and not a multiple of 100
"""

def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Enter a year to check if it is a leap year: "))
result = check_leap_year(year)
print(result)
