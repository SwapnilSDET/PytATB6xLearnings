count = 0

def increment():
    global count
    count = count + 1

increment() #1
increment() #2
increment() #3
print(count)