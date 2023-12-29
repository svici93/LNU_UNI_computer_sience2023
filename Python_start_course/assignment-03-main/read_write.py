import os


def read_file(file_path):

    with open(file_path, "r") as file:

        lst = []
        for line in file:
            lst.append(line.strip())

    return lst


def write_file(lines, file_path):
    with open(file_path, "w") as file:

        for line in lines:
            file.write(line + "\n")


path_read = os.getcwd() + "/mamma_mia.txt"
path_write = os.getcwd() + "/output.txt"

write_file(read_file(path_read), path_write)
