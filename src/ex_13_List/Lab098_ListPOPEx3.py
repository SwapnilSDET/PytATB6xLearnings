squares = [1, 4, 9, 16, 25]
print(squares.pop())  # 25 - Remove and return an item at index (default last element)
print(squares)  # [1, 4, 9, 16]
print(squares.pop(1))  # 4
print(squares)  # [1, 9, 16]

squares.clear()
print(squares)  # [] - Deleted all the elements from the list

# index(element, start, end)
# Returns the index of the first occurrence of the element.
numbers = [10, 20, 30, 20, 40]
print(numbers.index(20))  # 1 - This will return the index of an element

print(numbers.count(20))  # 2 - This will return a number of count for the occurrence of an element

numbers.sort()  # This will sort and return the list
print(numbers)  #

numbers.sort(reverse=True)  # This will reverse sort and return the list
print(numbers)

numbers.reverse()  # reverse() - Reverses the list in place.
print(numbers)

# max() / min() / sum() Works for numerical lists.
print(max(numbers))  # 40
print(min(numbers))  # 10
print(sum(numbers))  # 120

# Slicing
print(numbers)  # [10, 20, 20, 30, 40]
print(numbers[1:4])  # from index of 1 to 3
print(numbers[-1])  # returns last element

print("apple" in numbers)  # False
print(20 in numbers)  # True

# List Creation and Comprehension
# range(1,5) -> list
l = list(range(1, 5))
print(l)  # 1,2,3,4

# Nested Lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])

# del statement - Deletes an element by index or the whole list.
# Delete is a keyword and remove is a function.
del numbers[0]
print(numbers)