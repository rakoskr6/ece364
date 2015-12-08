#! /usr/bin/env python

#     $Author: ee364 $
#       $Date: 2001/11/02 19:48:40 $
#   $Revision: 1.1 $

from Tkinter import *
from Buttons import *
from tkMessageBox import askokcancel
import sys


def Quit():
    Reply = askokcancel("Verify Quit",
            "Do You really want to Quit")
    if Reply != 0:
        Root.destroy()

def Send_Message():

    Win = Toplevel()
    Win.title("Message Window")
    Win.config(bg="light yellow", cursor="gobbler")

    Info = Message(Win, text="EE 364 is the best ECE class\nHello!\nHi!",
                   bg="light green", fg="red",
                   font=("Times", 24, "bold"))
    Info.pack(side=TOP)

    Win.focus_set()
    Win.grab_set()
    Win.wait_window()
 
Root = Tk()
Root.title(sys.argv[0])
Root.config(bg="light green")
Root.protocol("WM_DELETE_WINDOW", Root.quit)

Quit_Button = My_Button()
Quit_Button.config(text="Quit", command=Quit)

Message_Button = My_Button()
Message_Button.config(text="SEND A MESSAGE", command=Send_Message)
Message_Button.config(bg="orange")


Root.mainloop()

