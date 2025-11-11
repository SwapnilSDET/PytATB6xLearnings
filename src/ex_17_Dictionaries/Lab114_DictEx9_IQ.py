#  Remove duplicate values from a dictionary.

input_dict = {"a": 1, "b": 2, "c": 1, "d": 3}

unique_values = set()
result = {}

# dict.items() - Return a set-like (key-value) object providing a view on the dict's items.

for key, value in input_dict.items():
    if value not in unique_values:
        result[key] = value
        unique_values.add(value)

print(result)