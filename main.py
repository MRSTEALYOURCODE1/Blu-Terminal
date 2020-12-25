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


inputs(version)

