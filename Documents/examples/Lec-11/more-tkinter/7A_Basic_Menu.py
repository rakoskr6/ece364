#! /usr/bin/env python

#     $Author: ee364 $
#       $Date: 2001/11/02 19:48:40 $
#   $Revision: 1.1 $

from Tkinter import *
from Buttons import *
from tkMessageBox import *

import sys


def Quit():
    Reply = askokcancel("Verify exit",
             "Really want to quit?")
    if Reply != 0:
        Root.destroy()

def Not_Done_Yet():
    print "Sorry -- Not implemented yet"

def Gen_Menu (Master):
    Top = Menu(Master)
    Master.config(menu=Top)
    
    File = Menu(Top)
    File.add_command(label="Select a file to use", command=Not_Done_Yet)
    File.add_command(label="Open the file", command=Not_Done_Yet)
    File.add_command(label="Close the file", command=Not_Done_Yet)
    File.add_command(label="Quit", command=Quit)
    Top.add_cascade(label="File", menu=File)
    
     
       
Root = Tk()
Root.title(sys.argv[0])
Root.config(bg="light green")
Root.protocol("WM_DELETE_WINDOW", Root.quit)

Header = Label(Root, text="Try out the menu options", 
                fg="Red", bg="beige",
                font=("courier", 24, "bold"))
Header.pack(side=TOP, expand=YES, fill=BOTH)

Gen_Menu(Root)

Quit_Button = My_Button()
Quit_Button.config(text="Quit", command=Quit)

Root.mainloop()
