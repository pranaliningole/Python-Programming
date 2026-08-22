import os

# specify the directory you want to list
directory = "."

# list all the files and directories in the specified path
contents = os.listdir(directory)

# Print each file and directory name 
for item in contents:
    print(item)