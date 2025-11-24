"""
Question - ✅Palidrome of String
🧩 Example Walkthrough
Let’s take the word "level":
Forward: "level"
Backward: "level"
Both are identical → Palindrome ✅

Now, "hello":
Forward: "hello"
Backward: "olleh"
Not the same → Not a palindrome ❌
"""


def isPalindrome(user_input):

    user_input = user_input.lower() # String converted into lower case

    for i in range(len(user_input)//2):
        if user_input[i] != user_input[len(user_input)-1-i]:
            return False

    return True

user_input = input("Enter a string: ")

if isPalindrome(user_input):
    print("The entered string is Palindrome")
else:
    print("The entered string is Not a palindrome")