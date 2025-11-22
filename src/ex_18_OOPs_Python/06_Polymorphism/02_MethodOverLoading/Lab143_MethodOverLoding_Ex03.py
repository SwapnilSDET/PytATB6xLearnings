class Person:

    def say_name(self, name):
        print("Hi,", name)

    def say_name(self, name, lastname = "Padekar"):
        print("Hi,", name, lastname)

t = Person()
t.say_name("Swapnil")

# In case of method overloading,
# when a function is available with same name but with additional parameters
# - then the function with max parameters will be used.