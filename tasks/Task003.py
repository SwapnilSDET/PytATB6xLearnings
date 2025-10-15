# Write a Python program to calculate the
# area of a circle given its radius using the formula area=п×г^2``` (Take pie as 3.14)
# I/P (r) - Float
# O/P - String formatted output of area

radius = float(input("Enter the radius"))
pi = 3.14
area_of_circle = pi * (radius * radius)

area = str(area_of_circle)
print(area)