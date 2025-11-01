# Scope of the variable

pb_global_b = 12 # Global variable - throughout the program

def my_function():
    pb_a = 10 # Local variable - limited to function
    print("Calling local variable within functional scope: ",pb_a) # 10
    print("Calling global variable within functional scope: ", pb_global_b) #12

# print(pb_a) # Can't be accessed outside the function
print("Calling global variable out of functional scope: ", pb_global_b) #12


my_function()