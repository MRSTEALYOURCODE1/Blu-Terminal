#!/usr/bin/env

import json
import pickle
import code
import os
import getpass

from colorama import init
init()
from colorama import Fore, Back, Style


import datetime
version = "1.0"

#space
print()
#space



def paskeys():
    filecheck = os.path.exists("more/data/paskeys.json")
    if filecheck == True:
        with open('more/data/paskeys.json') as f:
            dataa = json.load(f)

        pwdchk = getpass.getpass("Enter Password: Secure 1.0$ ")
        if pwdchk == dataa['pwd']:
            print()
            print(Fore.GREEN + "Welcome Back")
            print(Style.RESET_ALL)
        else:
            print(Fore.RED + "Incorrect")
            paskeys()


        
paskeys()



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
        print(Fore.GREEN + "[Process Completed]")
        quit()

    if user_input == "keys":
        print("Keys-Are:")
        inputs(version)

    if user_input == "-sp-" or user_input == "set password" or user_input == "Set Pwd" or user_input == "set pwd" or user_input == "Set Password" or user_input == "SET PASSWORD":
        filecheck = os.path.exists("more/data/paskeys.json")
        if filecheck == False:
            data = {}
            data['pwd'] = getpass.getpass("Set Password $ ")
            writeToJSONFile('','more/data/paskeys',data)
            inputs(version)
        else:
            print("You Already Have A Password")
            inputs(version)

    if user_input == "time" or user_input == "Time" or user_input == "TIME":
        now = datetime.datetime.now()
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        inputs(version)

    if user_input == "text" or user_input == "editor" or user_input == "Text" or user_input == "TEXT":
        os.system('python3 more/code.py')
        print("Your Back!!")
        inputs(version)

    if user_input == "calculator" or user_input == "-c-" or user_input == "Calculator" or user_input == "CALCULATOR":
        while True:
            num1 = input("Calculator 1.0$ ")

            check = num1.isnumeric()

            while check == False:
                if num1 == "":
                    break

                if num1 == "q" or num1 == "quit" or num1 == "Quit" or num1 == "QUIT" or num1 == "Q":
                    break
                    
                print("Error Bad Input")
                num1 = input("Calculator 1.0$ ")
                check = num1.isnumeric()

            while num1 == "":
                num1 = input("Calculator 1.0$ ")

            if num1 == "done" or num1 == "q" or num1 == "quit":
                inputs(version)
                exit()

            num1 = int(num1)

            

            

            

            op = input("Calculator 1.0$ ")

            while op != "x" or op != "+" or op != "/" or op != "-" or op != "÷":
                if op == "":
                    break
                if op == "x" or op == "+" or op == "/" or op == "-" or op == "÷":
                    break
                if op == "q" or op == "quit" or op == "Quit" or op == "QUIT" or op == "Q":
                    break
                print("Error Bad Operator")
                op = input("Calculator 1.0$ ")

            while op == "":
                op = input("Calculator 1.0$ ")

            if op == "done" or op == "q" or op == "quit":
                inputs(version)
                exit()

            num2 = input("Calculator 1.0$ ")

            check2 = num2.isnumeric()

            while check2 == False:
                if num2 == "":
                    break

                if num2 == "q" or op == "quit" or op == "Quit" or op == "QUIT" or op == "Q":
                    break
                
                print("Error Bad Input")
                num2 = input("Calculator 1.0$ ")
                check = num2.isnumeric()

            while num2 == "":
                num2 = input("Calculator 1.0$ ")

            if num2 == "done" or num2 == "q" or num2 == "quit":
                inputs(version)
                exit()


            num2 = int(num2)

            if op == "x":
                print(num1 * num2)
                inputs(version)
                exit()
            elif op == "+":
                print(num1 + num2)
                inputs(version)
                exit()
            elif op == "/" or op == "÷":
                print(num1 / num2)
                inputs(version)
                exit()
            elif op == "-":
                print(num1 - num2)
                inputs(version)
                exit()
            

            
        


    if user_input == "Amitoj":
        print("You Have Found The Secret Name Of Whom Made This BootLeg Bash")
        inputs(version)

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



def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)


inputs(version)

