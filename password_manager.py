from secret import get_master_pwd
from menu import mainMenu, create, find_accounts, find


secret = get_master_pwd()


def runProgram():
    passw = input('Hello master, please start by providing the master password: ')

    if passw == secret:
        print('You\'re in')
        menuChoice = mainMenu()
        if menuChoice == '1':
            create()
        elif menuChoice == '2':
            find_accounts()
        elif menuChoice == '3':
            find()
        elif menuChoice == 'Q':
            exit()
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
