#password manager
import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.title("Password Manager")
window.minsize(550,210)


def submitName():
    nameQuery.configure(text = 'Hello, ' + name.get())

    nameEntered.place(x=250,y=80,anchor="center")
    passwordEntered.place(x=250,y=80,anchor="center")
    passwordQuery.place(x=250,y=65,anchor="center")
    button1.place(x=190, y=110)
    button2.place(x=190, y=110)  

def submitPass():
    passwordQuery.configure(text = 'Are you sure you want to use, ' + passwordEntered.get() + 'as your main file password?')



name = tk.StringVar()
nameEntered = tk.Entry(window, width = 15, textvariable = name)
nameQuery = tk.Label(
    text = "What is your name?",
    foreground="black", 
    background = "white"
)


filePass = tk.StringVar()
passwordEntered = tk.Entry(window, width = 25, textvariable = filePass)
passwordQuery = tk.Label(
    text = "Type your main password.",
    foreground="black", 
    background = "white"
)


button1 = ttk.Button(window, text = "Enter name", command = submitName)
button2 = ttk.Button(window, text = "Enter password", command = submitPass)

nameQuery.place(x=250,y=40,anchor="center")
nameEntered.place(x=192, y=60)
button1.place(x=210, y=90)

window.mainloop()

#steps (assuming its the first time)
    #run program
    #asks for name
    #ask for password for protected file
    #confirm password with user
    #start creation of the password protected file with 7-zip file called (name)-Passwords on Desktop
     #checks if file does not already exist and 
     #if it does not already exist, continues creating file
     #else tell user file already exist and pompt for new name
    #let user know that file is created on dektop and shows password

#steps (assuming password file exist)
    #checks that file actually exist
     #if it does ask for password to file
    #prompt for adding new username/email and password 
    #confirm with displaying typed values (repsonese with Y or N)?
    #Once confimed: display confirmtion
    #promost for adding new uesername/email


