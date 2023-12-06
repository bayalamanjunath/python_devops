#numbers = input("print numbers") 

import os

folder_list = input("give the path to list the folder:  "  ).split()

for folders in folder_list:
  list_folders = os.listdir(folders)
  print("==============list of folders inside path" + folders)
  #print(list_folders)
  for folder in list_folders:
    print(folder)
