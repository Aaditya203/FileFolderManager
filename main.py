from pathlib import Path
import os
import shutil
import speech_recognition as sr
from gtts import gTTS
from tempfile import NamedTemporaryFile
from playsound import playsound


def speak(text):
    fs = NamedTemporaryFile(delete=False,suffix=".mp3")
    temp_path = fs.name
    fs.close()
    tts = gTTS(text=text,lang='en')
    tts.save(temp_path)
    playsound(temp_path)
    os.remove(temp_path)

def create_folder():
    try:
        speak("Enter the folder name")
        name = input("Enter the folder name: ")
        p = Path(name)
        if p.exists():
            raise Exception("File already exists!")
        else:
            p.mkdir()
            print("Folder Created Successfully!!")
            speak("Folder Created Successfully!!")


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
    # read_file_folder()
    try:
        speak("Enter the name of folder you want to change: ")
        old_name = input("Enter the name of folder you want to change: ")
        p = Path(old_name)
        if p.exists():
            speak("Enter the new name of the folder: ")
            new_name = input("Enter the new name of the folder: ")
            new_p = Path(new_name)
            p.rename(new_p)
            print("Renamed Successfully!")
            speak("Renamed Successfully!")
        else:
            print("Folder name dont exists!!")
            speak("Folder name dont exists!!")
    except Exception as e:
        print(f"Some error occurred: {e}")    


def delete_folder():
    try:
        speak("Enter the name of folder you want to delete: ")
        name = input("Enter the name of folder you want to delete: ")
        p = Path(name)
        if p.exists():
            shutil.rmtree(p)
            print("Deleted Successfully!!")
            speak("Deleted Successfully!!")
        else:
            print("No folder exists with that name!!")
            speak("No folder exists with that name!!")

    except Exception as e:
        print(f"Some error occurred: {e}")    

def create_file():
    try:
        speak("Enter the file name with extension: ")
        name = input("Enter the file name with extension: ")
        p = Path(name)
        if p.exists():
            print("File already exists!!")
            speak("File already exists!!")
            
        else:
            with open(p,'w') as fs:
                fs.write("")
            print("file create successfully!!")
            speak("file create successfully!!")
            
    except Exception as e:
        print(f"Some error occurred as {e}")

def read_file():
    try:
        speak("Enter the name of file you want to read with extension: ")
        name = input("Enter the name of file you want to read with extension: ")
        p = Path(name)
        if p.exists():
            with open(p,'r') as fs:
                print(fs.read())
        else:
            print("File doesn't exists!")
            speak("File doesn't exists!")
    except Exception as e:
        print(f"Error occurred: {e}")

def update_file():
    try:
        speak("Enter the name of file which you want to update: ")
        name = input("Enter the name of file which you want to update: ")
        p = Path(name)
        if p.exists():
            print("Option to do updation on a file")
            print("1. For writing a file")
            print("2. For appending a data in a file")
            print("3. For renmaing a file")

            speak("Option to do updation on a file")
            speak("1. For writing a file")
            speak("2. For appending a data in a file")
            speak("3. For renmaing a file")

            speak("Enter what you want to do : ")
            want = int(input("Enter what you want to do : "))
            if want == 1:
                with open(p,'w') as fs:
                    speak("Enter the file content you want to add: ")
                    content = input("Enter the file content you want to add: ")
                    fs.write(content)
                
            elif want ==2:
                with open(p,'a') as fs:
                    speak("Enter the file content you want to append: ")
                    content = input("Enter the file content you want to append: ")
                    fs.write(content)
            elif want==3:
                speak("Enter the newname of the file with extension: ")
                new_name = input("Enter the newname of the file with extension: ")
                new_p = Path(new_name)
                p.rename(new_p)

        else:
            print("File doesn't exists!")
            speak("File doesn't exists!")
    
    except Exception as e:
        print(f"Some Error Occurred as {e}")

def delete_file():
    try:
        speak("Enter the name of file you want to delete")
        name = input("Enter the name of file you want to delete")
        p=Path(name)
        if p.exists():
            os.remove(p)
            speak("Deleted successfully")
        else:
            print("File not exist!")
            speak("File not exist!")
    except Exception as e:
        print(f"Some error occured as {e}")

print("For folder related operations click 1 and for file related operations click 2: ")

speak("For folder related operations click 1 and for file related operations click 2: ")

speak("Enter a number")

opt = int(input("Enter a number: "))
if opt == 1:
    print("Options to perform Folder handling: ")

    print("1. Create folder")
    print("2. Read files and folder inside that folder")
    print("3. Update folder")
    print("4. Delete folder")

    speak("Options to perform Folder handling: ")
    speak("1. Create folder")
    speak("2. Read files and folder inside that folder")
    speak("3. Update folder")
    speak("4. Delete folder")

    speak("Enter the choice which you want to perform on folder ")
    choice = int(input("Enter the choice which you want to perform on folder for handling it: "))

    if choice == 1:
        create_folder()
    elif choice == 2:
        read_file_folder()
    elif choice == 3:
        update_folder()
    elif choice == 4:
        delete_folder()
elif opt ==2:

    print("options to perform File Handling: ")
    print("1. Create file")
    print("2. Read a file")
    print("3. Update a file")
    print("4. Delte a file")

    speak("options to perform File Handling: ")
    speak("1. Create file")
    speak("2. Read a file")
    speak("3. Update a file")
    speak("4. Delte a file")

    speak("Enter the choice which you want to perform on file: ")
    choice = int(input("Enter the choice which you want to perform on file: "))
    if choice == 1:
        create_file()
    elif choice == 2:
        read_file()
    elif choice == 3:
        update_file()
    elif choice == 4:
        delete_file()
    