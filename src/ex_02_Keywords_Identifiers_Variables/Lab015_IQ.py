"""
print("Hello" + 15)
Python - No Concatenation Concept for incompatible data types

This will show error like below -
Traceback (most recent call last):
      print("Hello" + 15)
          ~~~~~~~~^~~~
TypeError: can only concatenate str (not "int") to str
"""

# If you want to print you need to convert all the variables in str
print("Hello" + str(15)) # Hello15

