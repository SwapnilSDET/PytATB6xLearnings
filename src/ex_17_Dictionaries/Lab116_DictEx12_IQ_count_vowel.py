input_string = "Hello, World"

# a,e,i,o,u - Vowels, rest of all are - Consonants

vowels = "aeiou"

vowels_count =0
result = list()

for char in input_string:
    if char in vowels:
        vowels_count += 1
        result.append(char)

print("The count of vowels are -> ",vowels_count)
print("List of vowels are -> ", result)