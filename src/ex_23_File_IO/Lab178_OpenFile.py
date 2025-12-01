# t = open('testdata.txt','r') - read mode
# t = open('testdata.txt','w') - write
# t = open('testdata.txt', 'r+') - read + write
# t = open('testdata.txt', 'w+') - read + write
# t = open('testdata.txt', 'b') - binary
# t.close() - This step is must to close the file.

# If we need to close the file automatically
with open('testdata.txt', 'r') as f:
    data = f.read()

print(data)
