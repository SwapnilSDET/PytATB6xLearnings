"""
In automation, you often compare expected and actual outputs.
Write code to check if a test case passed or failed.

expected_title = "Dashboard"
actual_title = "Dashboard "

✅ Test Passed – Title matches
❌ Test Failed – Title doesn't match

Should be True - why > Strip and convert them into the lowercase = both of them are equal.
"""


expected_title = "Dashboard"
actual_title = input("Enter the actual_title: ").strip()

if expected_title.lower() == actual_title.lower():
    print("✅ Test Passed – Title matches")
else:
    print("❌ Test Failed – Title doesn't match")