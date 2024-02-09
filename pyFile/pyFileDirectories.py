import os

def create_subDirectories(parent_dir,num_subDirectories):
    while num_subDirectories != 0:
        subDirectory_name = input("\nSet the name of the sub directory for your path: ")
        path = os.path.join(parent_dir,subDirectory_name)
        os.makedirs(path)
        num_subDirectories -= 1
        print("Sub directory '%s' created" % subDirectory_name)

parent_dir = str(input("Type the parent directory that you want: "))
print("The Path of the program is {}\n".format(parent_dir))
num_subDirectories = int(input("Type an number to the amount of subdirectories: "))

create_subDirectories(parent_dir,num_subDirectories)

