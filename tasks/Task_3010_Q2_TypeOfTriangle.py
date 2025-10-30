"""
Q2 - Create a function which will take the 3 values from the user, which are length of the triangle.  side1, side2, side2
i/p - int side1 == side2 == side3 → isoceles
o/p = result in string - iso, eq, scalene
"""


def validate_type_of_triangle(side1, side2, side3):
    if side1 == side2 and side2 == side3:
        print("This is a Equilateral triangle")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("This is a Isosceles triangle")
    else:
        print("This is a Scalene triangle")


side1 = int(input("Enter length of side1: "))
side2 = int(input("Enter length of side2: "))
side3 = int(input("Enter length of side3: "))

validate_type_of_triangle(side1, side2, side3)