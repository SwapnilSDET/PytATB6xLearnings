class TestCounter:
    count = 0

    def __init__(self):
        TestCounter.count += 1 # ClassName.Variable is direct accessible

t1 = TestCounter() #1
t2 = TestCounter() #2
print(TestCounter.count) # 2

# Each time an object is created, count increases.
# count is shared across all objects.