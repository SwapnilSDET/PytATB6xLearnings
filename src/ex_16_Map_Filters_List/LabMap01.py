# map(function, iterable)
# Applies a function to each item in a list (or any iterable) and returns a map object (iterator).

 
numbers = [1, 2, 3, 4, 5]


def square(x):
    return x ** 2


sq_all_numbers = list(map(square, numbers))
print(sq_all_numbers) # [1, 4, 9, 16, 25]

