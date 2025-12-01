import os

# print(os.name) # To print operating system's name nt - Windows
# print(os.getcwd()) # To print the current working directory's path

# os.mkdir("AI")
print(os.listdir(os.getcwd())) # This will print all the files and folders in the directory.


print(os.listdir())

#print(os.remove("AI.txt"))
print(os.rename("AI.txt", "AI/testdata.txt"))

# print(os.environ.get("PATH"))