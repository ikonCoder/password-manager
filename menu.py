from db_controller import store_accountInfo, searchByEmail, searchByPassword


def mainMenu():
    print('-' * 30)
    print(('-' * 13) + 'Menu' + ('-' * 13))
    print('1. Create new user info')
    print('2. Find all sites and apps connected to an email')
    print('3. Find a password for a site or app')
    print('Q. Exit')
    print('-' * 30)
    return input(': ')


# creates new account info
def create():
    print('-' * 13 + "ACCOUNT  CREATION" + '-' * 13)
    newApp = input("What app/website is this password for?: ")
    newPassword = input("Enter your new password: ")
    newEmail = input("Enter the email associated with this account (TYPE NONE IF NOT REQUIRED): ")
    newUsername = input("Enter the username associated with this account (TYPE NONE IF NOT REQUIRED): ")

    # Rename variables for db_controller (not necessary, but makes it cleaner)
    password = newPassword
    username = newUsername
    email = newEmail
    app_name = newApp

    # This will leave the entry blank when inserting into the db
    if newUsername is None:
        username = ''
    if newEmail is None:
        email = ''

    print("ADDING INFO TO DATABASE.....")
    store_accountInfo(password, username, email, app_name)


# account finder (by email)
def find_accounts():
    print('-' * 13 + "ACCOUNT FINDER (BY EMAIL)" + '-' * 13)
    emailQuery = input("Enter the email you'd like to use: ")
    email = emailQuery

    print("SEARCHING DATABASE......")
    searchByEmail(email)


# account finder (by password)
def find():
    print('-' * 13 + "ACCOUNT FINDER (BY PASSWORD)" + '-' * 13)
    pwrdQuery = input("Enter the password you'd like to use: ")
    pwrd = pwrdQuery

    print("SEARCHING DATABASE......")
    searchByPassword(pwrd)


def exit():
    print("Goodbye, master")
    quit()
    


