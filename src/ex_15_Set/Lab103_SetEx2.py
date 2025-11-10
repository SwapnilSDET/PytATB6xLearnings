# Union, Intersection, Difference, Symmetric Difference

a = {1, 2, 3}
b = {3, 4, 5}

# Union - All the values are shown, duplicates only once.
print(a | b)  # {1, 2, 3, 4, 5}
print(a.union(b))  # {1, 2, 3, 4, 5}

# Intersection - All the COMMON values are shown.
print(a & b)  # {3}
print(a.intersection(b))  # {3}

# Difference - This will keep the elements present in a, but not in b.
print(a - b)  # {1, 2}
print(a.difference(b))  # {1, 2}

print(b - a)  # {4, 5}
print(b.difference(a))  # {4, 5}

# Symmetric Difference - Common elements are removed and remaining set is delivered.
print(a ^ b)  # {1, 2, 4, 5}
print(a.symmetric_difference(b))  # {1, 2, 4, 5}

# -------------------------------------------------------------

set1 = {1, 2, 3}
set2 = {4, 5, 6}
my_set = set1.union(set2)
print(my_set) # {1, 2, 3, 4, 5, 6}

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

my_set = set1.intersection(set2)
print(my_set) # {4, 5}

my_set = set1.difference(set2)
print(my_set) # {1, 2, 3}

my_set = set2.difference(set1)
print(my_set) # {8, 6, 7}