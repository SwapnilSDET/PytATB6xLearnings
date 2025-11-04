"""
Q2 - Create a function which will take the 3 values from the user, which are length of the triangle.  side1, side2, side2
i/p - int side1 == side2 == side3 → isoceles
o/p = result in string - iso, eq, scalene
"""


def classify_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0: # Sides should be greater than 0.
        if a + b > c and b + c > a and c + a > b: # Sum of 2 sides should be greater than the third side.
            if a == b == c: # If all sides are same
                return "This is a Equilateral triangle"
            elif a == b or b == c or a == c: # If any 2 sides are same
                return "This is a Isosceles triangle"
            else: # No sides are same
                return "This is a Scalene triangle"
        else:
            return "This is not a triangle"
    else:
        return "You might have entered an invalid values for side1, side2, side3"


side1 = float(input("Enter length of side1: "))
side2 = float(input("Enter length of side2: "))
side3 = float(input("Enter length of side3: "))

result = classify_triangle(side1, side2, side3)
print(f"The triangle is classified as: {result}")
