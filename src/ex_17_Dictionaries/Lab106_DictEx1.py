# Dictionaries are mutable, unordered, Key-Value pair structure
# Syntax - dict_name = {"Key":"Value"}
# OR dict_name = dict(key="Value")
# e.g. student_infor2 = dict(name="Pramod", age=67, address="KA")


my_dict = {
    "name": "Aman",
    "age": 34,
    "role": "SDET",
    "exp": 3

}

print(my_dict) # {'name': 'Aman', 'age': 34, 'role': 'SDET', 'exp': 3}
print(my_dict["age"]) # 34
print(my_dict["role"]) # SDET

my_dict["role"] = "Manual Tester"
print(my_dict) # {'name': 'Aman', 'age': 34, 'role': 'Manual Tester', 'exp': 3}

del my_dict["age"]
print(my_dict) # {'name': 'Aman', 'role': 'Manual Tester', 'exp': 3}

for key, value in my_dict.items():
    print(key, value)

# name Aman
# role Manual Tester
# exp 3

print("age" in my_dict) # False
print("role" in my_dict) # True
