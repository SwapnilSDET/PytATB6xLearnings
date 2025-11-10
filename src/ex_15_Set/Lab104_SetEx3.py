# Sets are mutable

set1 = set(["TheTestingAcademy", "For", "TheTestingAcademy."]) # Conversion of list to set
print(set1) # {'TheTestingAcademy.', 'For', 'TheTestingAcademy'}
print(type(set1)) # <class 'set'>
print(len(set1)) # 3

# Iteration within sets
for i in set1:
    print(i)

set1.add("Pramod")
set1.add("Pramod")
print(set1) # {'Pramod', 'TheTestingAcademy.', 'For', 'TheTestingAcademy'}