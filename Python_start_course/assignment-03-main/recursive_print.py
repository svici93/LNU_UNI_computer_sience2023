import os


def count_sub(dir_path):

    print(os.path.basename(dir_path))
    sub_dirs = [x for x in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, x))]
    for sub in sub_dirs:
        sub_path = os.path.join(dir_path, sub)
        count_sub(sub_path)


dir_path = os.getcwd()
count_sub(dir_path)
