def vwo_login(user):
    if user != "admin":
        raise Exception("Unauthorized access.")
    return "Welcome Admin"

# print(vwo_login("Swapnil")) # Exception: Unauthorized access.
print(vwo_login("admin")) # Welcome Admin