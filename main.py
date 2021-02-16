# password manager
import tkinter as tk
import os.path
from tkinter import ttk

window = tk.Tk()
window.title("Password Manager")

# Globals
protectedFileName = "pwdManager"
fileNameExtension = ".xml"


# functions
def quit():
    window.withdraw()

    # start the creation of password protected file
    # step1: check if the file already exist
    fileExist = os.path.isfile(protectedFileName + fileNameExtension)
    if fileExist:
        print("Password File already exist")
    else:
        print("Creating xml...")
        fileCreated = open(protectedFileName + fileNameExtension, "w")
        if fileCreated:
            print("File creation was a success!")


def submitName():
    nameQuery.configure(
        text='Hello, ' + name.get()
    )
    passwordTxtField.place(x=250, y=90, anchor="center")
    passwordQuery.place(x=250, y=65, anchor="center")
    submitPwdBtn.place(x=190, y=110)
    nameEntered.place_forget()
    nameSubmitBtn.place_forget()


def submitPass():
    passwordQuery.configure(
        text='Are you sure you want to use, ' + '"' + passwordTxtField.get() + '"' + ' as your main file password?'
    )
    # hide everything other than yes or no block
    submitPwdBtn.place_forget()
    passwordTxtField.place_forget()
    yesButton.place(x=170, y=90)
    noButton.place(x=270, y=90)


def pwdConfimed():
    print("password confirmed")
    quit()


def redoPwdInput():
    yesButton.place_forget()
    noButton.place_forget()

    submitPwdBtn.place(x=190, y=110)
    passwordTxtField.place(x=250, y=90, anchor="center")


# name strings and input boxes
name = tk.StringVar()
nameEntered = tk.Entry(window, width=15, textvariable=name)
nameEntered.place(x=192, y=60)
nameQuery = tk.Label(
    text="What is your name?",
    foreground="black",
    background="white"
)
nameQuery.place(x=250, y=40, anchor="center")
nameSubmitBtn = ttk.Button(window, text="Enter name", command=submitName)
nameSubmitBtn.place(x=210, y=90)

# password string and input boxes
filePass = tk.StringVar()
passwordTxtField = tk.Entry(window, width=25, textvariable=filePass)
passwordQuery = tk.Label(
    text="Type your main password.",
    foreground="black",
    background="white"
)
submitPwdBtn = ttk.Button(window, text="Enter password", command=submitPass)

# buttons
yesButton = ttk.Button(window, text="Yes", command=pwdConfimed)
noButton = ttk.Button(window, text="No", command=redoPwdInput)

window.mainloop()
# steps (assuming its the first time)
# run program
# asks for name
# ask for password for protected file
# confirm password with user
# start creation of the password protected file with 7-zip file called (name)-Passwords on Desktop
# checks if file does not already exist and
# if it does not already exist, continues creating file
# else tell user file already exist and pompt for new name
# let user know that file is created on dektop and shows password

# steps (assuming password file exist)
# checks that file actually exist
# if it does ask for password to file
# prompt for adding new username/email and password
# confirm with displaying typed values (repsonese with Y or N)?
# Once confimed: display confirmtion
# promost for adding new uesername/email
