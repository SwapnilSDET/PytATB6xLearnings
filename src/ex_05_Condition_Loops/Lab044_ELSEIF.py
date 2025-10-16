# Find the positive number is even or odd

num = int(input("Enter the number: ").strip())

# if num >=0:
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
# else:
#     print("Negative number")

# Alternate way to write above code in less lines
if num >= 0:
    print("Even" if num % 2 == 0 else "Odd")
else:
    print("Negative number")