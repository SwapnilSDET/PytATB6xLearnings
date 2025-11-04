def add_security(func):
    def wrapper():
        # Before
        print("1. Before the function is called.")
        print("2. Add Helmate, Dashcam, Gloves, Knee Guards, License")

        # Function call
        func()

        # After
        print("3. After the function is called.")
        print("4. Secure driving, Leave all the items")

    return wrapper()



@add_security
def drive_ola_scooter():
    print("I am driving ola scooter")
