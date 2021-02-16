from secret import get_master_pwd
from menu import mainMenu


secret = get_master_pwd()


def runProgram():
    passw = input('Hello master, please start by providing the master password: ')

    if passw == secret:
        print('You\'re in')
        mainMenu()
    else:
        choice = input('No luck...would you link to try again? Type YES or NO. ')
        if choice == 'YES':
            runProgram()
        elif choice == 'NO':
            exit()
        else:
            print("Not a valid response")
            runProgram()


runProgram()