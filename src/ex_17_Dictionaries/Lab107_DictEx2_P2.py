student_infor = {
    "name": "Swapnil",
    # "age": 65,
    "age": 39,  # In case of duplication, the latest value is kept
    "address": "Navi Mumbai"
}

print(student_infor)  # {'name': 'Swapnil', 'age': 39, 'address': 'Navi Mumbai'}
print(student_infor["name"])
print(student_infor["age"])
print(student_infor["address"])

student_infor["age"] = 100  # Values are mutable in Dicts
print(student_infor)  # {'name': 'Swapnil', 'age': 100, 'address': 'Navi Mumbai'}
