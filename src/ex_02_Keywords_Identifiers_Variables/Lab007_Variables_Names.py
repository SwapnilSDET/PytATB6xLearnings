#123abc=90 # Not allowed
_name = "Swapnil"
_age = 20
pi = 3.14
name = "Pramod"
isMale = True

"""
Type Function 
- Basically give you details about the data type of the variable. 
- type()
    - _pramod  = "amit"
`print(type(_pramod)) # <class 'str'>` 
"""
print(type(_name)) # <class 'str'>
print(type(_age)) # <class 'int'>
print(type(pi)) # <class 'float'>
print(type(name)) # <class 'str'>
print(type(isMale)) # <class 'bool'>

"""
Complex Numbers - 
DATA Type - Complex numbers - Python - iota
-  iota ->  root of - 1 ( i) ->  j
- complex_numbers = 2+3j -
- 2 -> Real number
- 3 - img ( j)  - j = rootof -1
"""
complex_number = 2+3j
print(complex_number) # (2+3j)
print(type(complex_number)) # <class 'complex'>
print(complex_number.real) # 2.0
print(complex_number.imag) # 3.0