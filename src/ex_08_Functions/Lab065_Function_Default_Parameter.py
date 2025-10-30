def greet_with_default_param(name="QA"):
    print("Hi,", name)


greet_with_default_param("Pramod") # Hi, Pramod
greet_with_default_param("Amit") # Hi, Amit
greet_with_default_param() # Hi, QA - When the parameter is not given then the default param is called.

