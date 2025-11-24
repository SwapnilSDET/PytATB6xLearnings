"""
Question - ✅ Count vowels and consonants in a String

Write a function & call it to view the result.

"""


input_str = input("Enter a string: ")
vowels = ("a", "e", "i", "o", "u")

def count_vowels_consonants(input_str):
    vowels_count = 0
    consonants_count = 0

    for char in input_str:
        if char in vowels:
            vowels_count += 1
        else:
            consonants_count += 1

    print("Count of vowels in entered string is => ", vowels_count)
    print("Count of consonants in entered string is => ", consonants_count)

count_vowels_consonants(input_str)
