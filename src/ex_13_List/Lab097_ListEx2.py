# Mutable - The list items can be changed.
# Indexation
# Append
# Extend
# Insert

my_list = [1, 2, 3, 4, 5]
print(type(my_list))
print(my_list)

# Indexing
print("Item at index 0 => ", my_list[0])  # 1
print("Item at index 1 => ", my_list[1])  # 2
print("Item at index 2 => ", my_list[2])  # 3
print("Item at index 3 => ", my_list[3])  # 4
print("Item at index 4 => ", my_list[4])  # 5

# Mutation
my_list[1] = "Swapnil"
my_list[2] = "Padekar"
print(my_list)

# How to iterate within the list
for item in my_list:  # No need of range
    print(item)

# range() - This also return the list
for i in range(1, 6):
    print(i)  # 1,2,3,4,5

# append() - Add object to the end of the list

my_list_new = [1, 2, 3, 4, 5]

my_list_new.append("Appended Item1")
print(my_list_new)
my_list_new.append("Appended Item2")
print(my_list_new)

# extend() - Append a new list at the end of the first one
my_list_new.extend([6, 7, 8, 9, 10])
print(my_list_new)

list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9, 10]
list_1.extend(list_2)
print(list_1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# insert() - Add an object at a specific position
my_list_ins = [1, 2, 3, 4, 5]
print("Length of the list before insertion => ", len(my_list_ins)) # 5
my_list_ins.insert(1, "Swapnil")
print("After inserting Swapnil at 1st position of the list => ", my_list_ins) # [1, 'Swapnil', 2, 3, 4, 5]
print("Length of the list after insertion => ", len(my_list_ins)) # 6

# remove a specific element
my_list_ins.remove("Swapnil")
print("After removing an element from the list => ", my_list_ins) # [1, 2, 3, 4, 5]

# Create a copy of the list
my_copy_list = my_list_ins.copy()
print("Copied list is => ", my_copy_list) # [1, 2, 3, 4, 5]

# Reverse the elements in the list
my_copy_list.reverse()
print("Reversed list is => ", my_copy_list) # [5, 4, 3, 2, 1]

