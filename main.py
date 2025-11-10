from pathlib import Path
import os
import shutil
import speech_recognition as sr
import pyttsx3


def create_folder():
    try:
        name = input("Enter the folder name: ")
        p = Path(name)
        if p.exists():
            raise Exception("File already exists!")
        else:
            p.mkdir()
            print("Folder Created Successfully!!")

    except Exception as e:
        print(f"Error occurred: {e}")

def read_file_folder():
    try:
        p = Path("")
        items = list(p.rglob('*'))
        for i,v in enumerate(items):
            print(f"{i+1}. {v}")
    except Exception as e:
        print(f"Some error occurred as {e}")

def update_folder():
    read_file_folder()
    try:
        old_name = input("Enter the name of folder you want to change: ")
        p = Path(old_name)
        if p.exists():
            new_name = input("Enter the new name of the folder: ")
            new_p = Path(new_name)
            p.rename(new_p)
            print("Renamed Successfully!")
        else:
            print("Folder name dont exists!!")
    except Exception as e:
        print(f"Some error occurred: {e}")    


def delete_folder():
    try:
        name = input("Enter the name of folder you want to delete: ")
        p = Path(name)
        if p.exists():
            shutil.rmtree(p)
            print("Deleted Successfully!!")
        else:
            print("No folder exists with that name!!")

    except Exception as e:
        print(f"Some error occurred: {e}")    

def create_file():
    try:
        name = input("Enter the file name with extension: ")
        p = Path(name)
        if p.exists():
            print("File already exists!!")
        else:
            with open(p,'w') as fs:
                fs.write("")
            print("file create successfully!!")
    except Exception as e:
        print(f"Some error occurred as {e}")

def read_file():
    try:
        name = input("Enter the name of file you want to read with extension: ")
        p = Path(name)
        if p.exists():
            with open(p,'r') as fs:
                print(fs.read())
        else:
            print("File doesn't exists!")
    except Exception as e:
        print(f"Error occurred: {e}")

def update_file():
    try:
        name = input("Enter the name of file which you want to update: ")
        p = Path(name)
        if p.exists():
            print("Option to do updation on a file")
            print("1. For writing a file")
            print("2. For appending a data in a file")
            print("3. For renmaing a file")

            want = int(input("Enter what you want to do : "))
            if want == 1:
                with open(p,'w') as fs:
                    content = input("Enter the file content you want to add: ")
                    fs.write(content)
                
            if want ==2:
                with open(p,'a') as fs:
                    content = input("Enter the file content you want to append: ")
                    fs.write(content)
            if want==3:
                new_name = input("Enter the newname of the file with extension: ")
                new_p = Path(new_name)
                p.rename(new_p)

        else:
            print("File doesn't exists!")
    
    except Exception as e:
        print(f"Some Error Occurred as {e}")

def delete_file():
    try:
        name = input("Enter the name of file you want to delete")
        p=Path(name)
        if p.exists():
            os.remove(p)
        else:
            print("File not exist!")
    except Exception as e:
        print(f"Some error occured as {e}")

print("For folder related operations click 1 and for file related operations click 2: ")
opt = int(input("Enter a number: "))
if opt == 1:
    print("Options to perform Folder handling: ")

    print("1. Create folder")
    print("2. Read files and folder inside that folder")
    print("3. Update folder")
    print("4. Delete folder")

    choice = int(input("Enter the choice which you want to perform on folder for handling it: "))

    if choice == 1:
        create_folder()
    if choice == 2:
        read_file_folder()
    if choice == 3:
        update_folder()
    if choice == 4:
        delete_folder()
elif opt ==2:
    print("options to perform File Handling: ")
    print("1. Create file")
    print("2. Read a file")
    print("3. Update a file")
    print("4. Delte a file")

    choice = int(input("Enter the choice which you want to perform on file: "))

    if choice == 1:
        create_file()
    if choice == 2:
        read_file()
    if choice == 3:
        update_file()
    if choice == 4:
        delete_file()