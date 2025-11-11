# function that returns the minimum and maximum value from a dictionary.
# {"a": 10, "b": 20, "c": 30}

# Defining function

def min_keys_dict(dictionary):
    return min(dictionary.keys())

def max_keys_dict(dictionary):
    return max(dictionary.keys())

def min_values_dict(dictionary):
    return min(dictionary.values())

def max_values_dict(dictionary):
    return max(dictionary.values())

dict1 = {"a": 10, "b":20, "c":30}
print("Key of lowest value: ", min_keys_dict(dict1))
print("Lowest value: ", min_values_dict(dict1))

print("Key of highest value: ", max_keys_dict(dict1))
print("Highest value: ", max_values_dict(dict1))