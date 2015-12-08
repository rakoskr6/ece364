#! /usr/bin/env python

#     $Author: ee364 $
#       $Date: 2001/11/02 19:48:40 $
#   $Revision: 1.1 $

from Tkinter import *
from Buttons import *
from tkMessageBox import askokcancel
import sys


def Quit():
    Reply = askokcancel("Verify exit",
             "Really want to quit?")
    if Reply != 0:
        Root.destroy()

def On_Press(I):
    States[I] = not States[I]

Root = Tk()
Root.title(sys.argv[0])
Root.config(bg="light green")
Root.protocol("WM_DELETE_WINDOW", Root.quit)

Header = Label(Root, fg="white", bg="blue",
           text="Check some boxes",
           font=("Helvetica", 24))
Header.pack(side=TOP, expand=YES, fill=BOTH)

States = []
for I in range(5):
   Check_Box = Checkbutton(Root, text=str(I),
               fg="Blue", bg="Light Blue",
               font=("Helvetica", 24, "bold"),
               activeforeground="Red",
               activebackground="Yellow",
               cursor="plus",
               command=(lambda I=I: On_Press(I)))
   Check_Box.pack(side=LEFT, expand=YES, fill=X)
   States.append(0)

Quit_Button = My_Button()
Quit_Button.config(text="Quit", command=Quit)


Root.mainloop()
print "Check_Box States", States

