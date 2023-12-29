import os


def mean(lst):

    return round(sum(lst)/len(lst), 1)


def std(lst):

    mu = mean(lst)
    diff = [(x - mu) ** 2 for x in lst]
    mu_2 = mean(diff)

    return round(mu_2 ** 0.5, 1)


def read_file1(pathTofile):
    numbers = []
    file = open(pathTofile, 'r')
    for line in file:

        integers = [int(num.strip()) for num in line.split(',')]

        numbers.extend(integers)
    return numbers


def read_file2(pathTofile):
    numbers = []
    file = open(pathTofile, 'r')
    for line in file:

        integers = [int(num.strip()) for num in line.split(':')]

        numbers.extend(integers)
    return numbers


path = os.getcwd()
file1 = f'''{path}/file_10k_integers/
file_10k_integers_A.txt'''.replace("\n", "")

file2 = f'''{path}/file_10k_integers/
file_10k_integers_B.txt'''.replace("\n", "")

lst1 = read_file1(file1)
lst2 = read_file2(file2)


print("Results for file A: ")
print(f"mean: {mean(lst1)}, standard deviation: {std(lst1)}\n")
print("Results for file B: ")
print(f"mean: {mean(lst2)}, standard deviation: {std(lst2)}")
