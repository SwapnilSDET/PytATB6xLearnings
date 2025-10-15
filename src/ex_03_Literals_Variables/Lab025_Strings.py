from logging import lastResort

name = "This is a big line"
print(type(name)) # <class 'str'>

name = name + str(1)
print(type(name)) # <class 'str'>

first_name = "Swapnil"
last_name = "Padekar"
full_name = first_name + " " + last_name
print(full_name) # Swapnil Padekar
print(type(full_name)) # <class 'str'>

