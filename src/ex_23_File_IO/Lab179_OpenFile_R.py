try:
    with open('testdata.txt','r') as file:
        # content = file.read()
        content = file.readlines() # This will print like a list
        print(content)

except FileNotFoundError as fnfe:
    print(fnfe)
