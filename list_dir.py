import os
folders = input("please provide the list of folders:\n ").split()
for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("please enter a valid folder name")
        continue
    except ZeroDivisionError:
        print("enter a valid numbere")
        break
    print("files in folder ===========  " + folder)
    for file in files:
        print(file)