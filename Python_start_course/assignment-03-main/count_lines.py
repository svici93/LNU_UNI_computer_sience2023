import os


def count_py_lines(dir_path):
    total_lines = 0
    # loop through all files in the path directory
    for item in os.listdir(dir_path):

        # generate path to all files in the directory
        item_path = os.path.join(dir_path, item)

        # check if file or dir
        if os.path.isdir(item_path):
            # If dir, recursively call the function
            total_lines += count_py_lines(item_path)

        # if file ends with .py
        elif item.endswith(".py"):

            # open file and count lines
            with open(item_path, "r") as f:

                lines = f.readlines()
                total_lines += len([line for line in lines if line.strip()])

    return total_lines


path = os.getcwd()
print(count_py_lines(path))
