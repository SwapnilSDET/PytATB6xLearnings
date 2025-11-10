# filter() - Filter elements based on a condition
# filter(function, iterable)
# Filters elements of an iterable using a condition (returns only those that match True).

nums = [1, 2, 3, 4, 5, 6]

def even_num(x):
    return x % 2 == 0

all_even_nums = list(filter (even_num, nums))
print(all_even_nums)

# --------------------------

list_student = [50, 51, 100]


def keep(x):
    if x > 50:
        return True


all_student = list(filter(keep,list_student))
print(all_student)