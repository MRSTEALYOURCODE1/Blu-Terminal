#!/usr/bin/env

import datetime
version = "1.0"

#space
print()
#space

now = datetime.datetime.now()
print("Blu Lanuched On:")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
print("--version--" + version)
print('To Quit Type "Quit" Or "Q"')
print('For Help Ask "Info"')

def inputs(version):
    user_input = input("Blu-" + version + "$ ")
    arguments(user_input)
    


def arguments(user_input):
    if user_input == "":
        inputs(version)
    
    if user_input == "info":
        print()
        print("Welcome To Blu")
        print("Here You Are Welcome To Download Almost Anything")
        inputs(version)

    if user_input == "Quit" or user_input == "quit" or user_input == "QUIT" or user_input == "q" or user_input == "Q":
        print("Bye!!")
        now = datetime.datetime.now()
        print("Blu Closed On:")
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        quit()

    if user_input == "keys":
        print("Keys-Are:")

    if user_input == "Amitoj":
        print("You Have Found The Secret Name Of Whom Made This BootLeg Bash")

    if user_input == "download":
        print("Download What?")
        print("  You Can Say:")
        print("   download Os")
        print("   download speech")
        print("   download tutorial")
        print("   download speech-to-text")
        print("   and much more")
        inputs(version)

    if user_input == "clear":
        i = 1
        while i < 100:
            i += 1
            print()
        inputs(version)

    print("Command Not Found")
    inputs(version)


inputs(version)

