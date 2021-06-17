
import os


# function that can be used to create a new directory


def create_new_directory():
    parent_directory = input("Enter path of parent_directory here:")
    new_directory = input("Enter name of new directory here:")
    path = os.path.join(parent_directory, new_directory)
    os.mkdir(path)
    print(f"Your new directory has been made at {parent_directory}.")


# same function as above but can now add multiple new directories at the same time with incremental numbers at the end.

def create_directories(numbers):
    parent_directory = input("Enter path of parent_directory here:")
    new_directory = input("Enter name of new directory here:")
    path = os.path.join(parent_directory, new_directory)
    for i in range(numbers):
        os.mkdir(path+"_"+str(i))
    print(f"Your new directories have been made at {parent_directory}.")
