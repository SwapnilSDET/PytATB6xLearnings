from collections import *

## Counter - data s

# user_input = input("Enter a String: ")
# count_char = Counter(user_input)
# print(count_char)

# namedtuple
# info = ('Swapnil', 39, 'ismarried', 'number')
# print(info)

info = namedtuple('info',['name', 'age', 'ismarried', 'number'])
t = info('Swapnil', 26, True, 1)

print(t) # info(name='Swapnil', age=26, ismarried=True, number=1)
print(t.name) # Swapnil
print(t.age) # 26
print(t.ismarried) # True
print(t.number) # 1