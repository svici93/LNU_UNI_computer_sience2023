import random


def count_occurrences(lst):
    occurrences = {}
    lst.sort()
    for element in lst:
        occurrences[element] = lst.count(element)

    return occurrences


lst = []
for i in range(1, 101):
    lst.append(random.randint(1, 10))

for key, value in count_occurrences(lst).items():
    print(key, " ", value)
