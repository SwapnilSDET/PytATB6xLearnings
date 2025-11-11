student_infor1 = {
    "name": "Swapnil",
    # "age": 65,
    "age": 67,
    "address": {
        "home_address": "Navi Mumbai",
        "office_address": "Pune"
    }
}

student_infor2 = {
    "name": "Snehal",
    # "age": 65,
    "age": 69,
    "address": {
        "home_address": "GOA",
        "office_address": "KA"
    }
}

# Converting as List of Dictionaries
student_list = [student_infor1, student_infor2]
print(student_list)
print(student_list[0])
print(student_list[0]["name"])
print(student_list[0]["address"]["office_address"])
