import os


def print_sub(dir_path, indent=""):
    print(indent + os.path.basename(dir_path))

    sub_dirs = [x for x in os.listdir(dir_path)
                if os.path.isdir(os.path.join(dir_path, x))]

    for sub in sub_dirs:
        sub_path = os.path.join(dir_path, sub)
        print_sub(sub_path, indent + "  ")


path = os.getcwd()
print_sub(path)
