"""
Check if the user can log in based on correct username and password.

I/p -> username = "admin" AND password = "1234"
O/p -> ✅ Login Successful
For the Fail condition Other O/P = ❌ Invalid Credentials
"""

exp_username = "admin"
exp_password = "1234"

act_username = input("Enter username: ").strip()
act_password = input("Enter password: ").strip()

if exp_username == act_username and exp_password == act_password:
    print("✅ Login Successful")
else:
    print("❌ Invalid Credentials")