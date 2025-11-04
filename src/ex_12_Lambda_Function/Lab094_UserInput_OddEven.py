"""
Write a Python program to calaculate even and odd numbers.

def find_even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
"""


number = int(input("Enter a number: "))

find_even_odd = lambda n: "Even" if n % 2 == 0 else "Odd"
# result = find_even_odd(number)
# print(result)
print(find_even_odd(number))