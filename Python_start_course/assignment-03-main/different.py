import random


def different(lst):
    s = set(lst)
    lst_output = list(s)

    lst_output.sort()
    return lst_output


lst = []
for i in range(1, 101):
    lst.append(random.randint(1, 200))

print(different(lst))
