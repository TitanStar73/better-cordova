WELC_DOC = """
Hey! Welcome to Cordova Creator tool by Arush Mundada
What would you like to do?
(1) Create new project
(2) Compile (without checking requirements)
(3) Compile a existing project (with checking requirements)
(4) All of the above!!
"""

from os import system as cmd
from os import path, getcwd, scandir
import tkinter as tk
from tkinter import filedialog

def browse_file():
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.withdraw()
    file_path = filedialog.askopenfilename()
    root.destroy()
    return file_path

if __name__ == "__main__":
    print(WELC_DOC)

    for i in range(0,10):
        try:
            MY_CHOICE = int(input("Enter choice from 1 to 4: "))
            break
        except ValueError:
            if i == 9:
                print("Please get help or read the docs.")
            else:
                print("Please enter a number from 1 to 4")
        except:
            MY_CHOICE = None
            break

    if MY_CHOICE == 1 or MY_CHOICE == 4:
        if any(scandir(getcwd())):
            print("THE CURRENT WORKING DIRECTORY IS NOT EMPTY")
            exit()
        
        PROJ_NAME = input("Enter project name (no spaces): ")
        DEV_NAME = input("Enter your developer/company name: ")
        DISPLAY_NAME = input("Enter display name: ")
        while True:
            VERSION = input("Enter version: ")
            if VERSION[0] == "0":
                print("CANNOT start with 0")
            else:
                try:
                    float(VERSION)
                    break
                except:
                    print("Should be a number")
                    
        DESCREPTION = input("Enter description (defaults to template): ")
        if DESCREPTION == "":
            DESCREPTION = f"An open-source ad-free {DISPLAY_NAME} made by a developer tired of ads on everything."

        LICENSE = input("Enter License (defaults to 'Apache-2.0'): ")

        DEV_EMAIL = input("Enter dev email (optional): ")
        DEV_EMAIL = "" if DEV_EMAIL == "" else f" email='{DEV_EMAIL}'"

        WEBSITE = input("Enter dev website (optional): ")
        WEBSITE = "" if WEBSITE == "" else f" href='{WEBSITE}'"
        
        while True:
            ICON_FILENAME = input("Enter complete icon filename or enter 'y' to browse (Ideally atleast 500x500 px, better-cordova will resize, place and seperate foreground and background for you!): ")
            if ICON_FILENAME == "y":
                ICON_FILENAME = browse_file()
                break
            elif path.exists(ICON_FILENAME):
                break
            
            print("Path does not exist.")

        ADD_PADDING = True if input("Would you like to add padding (recommended is 1/6 on all sides)? Enter y: ").lower() in {"yes","y","not no"} else False
        USE_SMART_STRIP = True if input("Is there a distinct background (Its ok if there isn't (: dw) (Saying yes to this will use a flood fill algorithm to seperate foreground and background which means you should close of pixels)? Enter y: ").lower() in {"yes","y","not no"} else False 
        inp = input("Enter platforms you would like. \n(1) android\n(2) iOS\n")
        indexfile = True if input("Enter y if you would like a default index file: ").lower() in {'y',"yes", "not no"} else False
        platforms = []
        for item in inp:
            if "1" in inp or "android" in inp.lower():
                platforms.append("android")
            if "2" in inp or "ios" in inp.lower():
                platforms.append("ios")

    
    if MY_CHOICE == 2:
        print(f"Started Compiling...\nYou cannot change anything in the directory while compiling.")        
        cmd(f"cordova build")

    if MY_CHOICE == 3 or MY_CHOICE == 4:
        print("Do you have the following requirements? (avdmanager only required if you want to run it on a virtual device)")
        cmd(f'cordova requirements')
        #ss
        print(f"You cannot change anything while compiling.")        
        while input("Type 'yes' to continue: ").lower() != 'yes':
            pass

        cmd(f"cordova build")

    print("Bye!")

#bat file to run this
#python "main.py" new %PluginType% %ProjectName% %DisplayName% %Author% %Description% %Confirm%

