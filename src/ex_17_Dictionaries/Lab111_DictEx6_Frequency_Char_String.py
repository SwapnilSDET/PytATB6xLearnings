# Frequency of Characters in a String
# Write a program to count the frequency
# of each character in a given string.
# string = "automation"
# {a : 2, u : 1 , t : 2 , o : 2, m : 1, i : 1, n : 1}
# ------------------------------------------------------
# Logic building
# I/P - string e.g automation
# O/P -> dict  # {a : 2, u : 1 , t : 2 , o : 2, m : 1, i : 1, n : 1}

string = input("Enter a string e.g automation: ")

char_count = {}

for char in string.lower():
        char_count[char] = char_count.get(char, 0) + 1
        # get() - Return the value for key if key is in the dictionary

print(char_count)

# O/P -
# Enter a string e.g automation: Automation
# {'a': 2, 'u': 1, 't': 2, 'o': 2, 'm': 1, 'i': 1, 'n': 1}

