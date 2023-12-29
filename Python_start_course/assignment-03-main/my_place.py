import os


def count_directories(path):
    entries = os.scandir(path)
    numberOfdirs = 0
    for entry in entries:
        if entry.is_dir():
            numberOfdirs += 1

    return numberOfdirs


def count_files(path):
    numberOffiles = 0
    entries = os.scandir(path)

    for entry in entries:
        if entry.is_file():
            numberOffiles += 1

    return numberOffiles


path = os.getcwd()

print(f"I am right now at: {path} \n" +
      f"Below me I have {count_directories(path)} directories/folders \n" +
      f"This directory contains {count_files(path)} files")
