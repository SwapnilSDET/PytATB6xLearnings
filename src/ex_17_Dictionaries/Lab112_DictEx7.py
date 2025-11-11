dict1 = {"a": 1, "b": 2, "c": 3}

print(dict1.keys()) # dict_keys(['a', 'b', 'c'])

print(dict1.values()) # dict_values([1, 2, 3])

print(dict1.items()) # dict_items([('a', 1), ('b', 2), ('c', 3)])


dict2 = {"a": 1, "b": 2}
missing_keys = dict1.keys() - dict2.keys()
print(missing_keys) # {'c'} - is missing in dict2
