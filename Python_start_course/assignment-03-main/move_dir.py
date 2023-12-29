import os


def list_dirs():
    path = os.getcwd()
    entries = os.scandir(path)

    for entry in entries:
        lst = []
        if entry.is_dir():
            lst.append(entry)
        return lst


def change_dir(str):

    os.chdir(str)


def lst_files():
    path = os.getcwd()
    entries = os.scandir(path)
    lst = []
    for entry in entries:
        if entry.is_file():
            lst.append(entry)
    return lst


while True:
    print("1. list directories.")
    print("2. change directory")
    print("3. List files")
    print("4. Exit program")

    userInput = int(input("\nPlease enter a command 1, 2, 3 or 4."))

    if userInput == 1:
        print("Folders are listed below: \n")
        print('\n'.join(map(str, list_dirs())))
        input("\nPress any key to continue..")

    elif userInput == 2:
        dir = input("Enter folder name or type .. to go back!")
        change_dir(dir)
        print(f"You are now currently in {os.getcwd()}")
        input("\nPress any key to continue..")

    elif userInput == 3:
        print("Folder contains following files: ")
        print('\n'.join(map(str, lst_files())))
        input("\nPress any key to continue..")

    elif userInput == 4:
        break
