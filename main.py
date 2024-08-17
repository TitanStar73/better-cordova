
WELC_DOC = """
Hey! Welcome to Cordova Creator tool by Arush Mundada
What would you like to do?
(1) Create new project
(2) Compile (without checking requirements)
(3) Compile a existing project (with checking requirements)
(4) All of the above!!
"""

from os import system as cmd
from os import getcwd, scandir


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
        #Create a new Project
    
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

