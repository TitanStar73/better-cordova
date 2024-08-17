WELC_DOC = """
Hey! Welcome to Cordova Creator tool by Arush Mundada
What would you like to do?
(1) Create new project
(2) Compile (without checking requirements)
(3) Compile a existing project (with checking requirements)
(4) All of the above!!
"""

from os import system as cmd
from os import chdir, path, getcwd, scandir
import json
from PIL import Image
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw

with open("main.js","r") as file:
    BASIC_JS_INDEX = file.read() 

with open("main.html","r") as file:
    BASIC_HTML_INDEX = file.read()

with open("main.css","r") as file:
    BASIC_CSS_INDEX = file.read()

def get_pixel_color(filename):
    with Image.open(filename) as img:
        color = img.getpixel((0, 0))
        hex_color = '#{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2])
        return hex_color

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
        
        
        cmd(f"cordova create {PROJ_NAME} com.{DEV_NAME.lower()}.{PROJ_NAME.lower()} {PROJ_NAME}")
        chdir(f"{PROJ_NAME}")
        for item in platforms:
            cmd(f"cordova platform add {item}")

        cmd("cordova plugin add cordova-plugin-android-permissions")

        config_xml = f"""
        <?xml version='1.0' encoding='utf-8'?>
        <widget id="com.{DEV_NAME.lower()}.{PROJ_NAME.lower()}" version="{VERSION}" xmlns="http://www.w3.org/ns/widgets" xmlns:cdv="http://cordova.apache.org/ns/1.0">
            <name>{PROJ_NAME}</name>
            <description>{DESCREPTION}</description>
            <author{DEV_EMAIL}{WEBSITE}>
                {DEV_NAME}
            </author>

            <content src="index.html" />
            <allow-intent href="http://*/*" />
            <allow-intent href="https://*/*" />
        </widget>
      """
        config_xml_root = f"""
        <?xml version='1.0' encoding='utf-8'?>
        <widget id="com.{DEV_NAME.lower()}.{PROJ_NAME.lower()}" version="{VERSION}" xmlns="http://www.w3.org/ns/widgets" xmlns:cdv="http://cordova.apache.org/ns/1.0" xmlns:android = "https://schemas.android.com/apk/res/android">
            <name>{DISPLAY_NAME}</name>
            <description>{DESCREPTION}</description>
            <author{DEV_EMAIL}{WEBSITE}>
                {DEV_NAME}
            </author>

            <platform name="android">
                <preference name="AndroidWindowSplashScreenAnimatedIcon" value="res/screen/android/splashscreen.png" />
                <preference name="AndroidWindowSplashScreenDuration" value="-1" /> <!-- Duration in milliseconds -->
                <preference name="SplashScreenBackgroundColor" value="{get_pixel_color(ICON_FILENAME).upper()}" /> <!-- Background color -->
            </platform>

            <content src="index.html" />
            <allow-intent href="http://*/*" />
            <allow-intent href="https://*/*" />
        </widget>
      """

        with open("config.xml","w+") as file:
            file.write(config_xml_root)
        with open("platforms/android/app/src/main/res/xml/config.xml","w+") as file:
            file.write(config_xml)

        with open('package.json', 'r') as file:
            data = json.load(file)

        data['name'] = f"com.{DEV_NAME.lower()}.{PROJ_NAME.lower()}"
        data['displayName'] = DISPLAY_NAME
        data['version'] = VERSION
        data['description'] = DESCREPTION
        data['scripts'] = {}
        data['author'] = DEV_NAME
        data['license'] = LICENSE if LICENSE != "" else "Apache-2.0"

        with open('package.json', 'w') as file:
            json.dump(data, file, indent=4)
        
        if indexfile:
            print("Writing basic index file...")
            with open('www/index.html',"w+") as file:
                file.write(BASIC_HTML_INDEX)
            with open('www/css/index.css',"w+") as file:
                file.write(BASIC_CSS_INDEX)
            with open('www/js/index.js',"w+") as file:
                file.write(BASIC_JS_INDEX)

        if USE_SMART_STRIP:
            def get_color_diff(color1, color2):
                return (color1[0] - color2[0])**2 + (color1[1] - color2[1])**2 + (color1[2] - color2[2])**2 + (color1[3] - color2[3])**2

            def generate_coords():
                start = 2
                while True:
                    for y in range(0,start+1):
                        yield (start-y,y)
                    start += 1

            with Image.open(ICON_FILENAME) as img_raw:
                tolerance = ((255 * (5 / 100))**2) * 4 #5 here is tolerance level in %
                width, height = img_raw.size
                img = img_raw.convert("RGBA")
                pixel_data = img.load()
                mask = Image.new('L', (width, height), 0)
                draw = ImageDraw.Draw(mask)
                our_stuff = img.getpixel((0,0))
                draw.point((0, 0), 255)
                draw.point((0, 1), 255)
                draw.point((1, 0), 255)
                
                for x,y in generate_coords():
                    if x >= width and y >= height:
                        break
                    for xt, yt in [(x-1,y-1), (x+1,y), (x,y+1), (x+1,y+1), (x-1,y+1), (x+1,y-1), (x-1,y), (x,y-1)]:
                        try:
                            if (mask.getpixel((xt,yt)) == 255) and get_color_diff(img.getpixel((0,0)), img.getpixel((x,y))) <= tolerance:
                                draw.point((x,y), 255)
                                break
                        except:
                            pass

                for xj,yj in generate_coords():
                    x = width - xj - 1
                    y = height - yj - 1
                    if x < 0 and y < 0:
                        break
                    for xt, yt in [(x-1,y-1), (x+1,y), (x,y+1), (x+1,y+1), (x-1,y+1), (x+1,y-1), (x-1,y), (x,y-1)]:
                        try:
                            if (mask.getpixel((xt,yt)) == 255) and get_color_diff(img.getpixel((0,0)), img.getpixel((x,y))) <= tolerance:
                                draw.point((x,y), 255)
                                break
                        except:
                            pass

                for x in range(width):
                    for y in range(height):
                        if mask.getpixel((x, y)) == 255:
                            pixel_data[x, y] = (255, 255, 255, 0)

                img.save(f'temporary_delete/foreground.png')

            with Image.open(ICON_FILENAME) as img_raw:
                width, height = img_raw.size
                img = img_raw.convert("RGBA")
                pixel_data = img.load()
                for x in range(width):
                    for y in range(height):
                        if mask.getpixel((x, y)) != 255:
                            pixel_data[x, y] = our_stuff
                img.save(f'temporary_delete/background.png')


    
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

