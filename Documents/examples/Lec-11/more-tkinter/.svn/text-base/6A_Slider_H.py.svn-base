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

       
def Print_Selection():
    print "Value selected:", Value.get()

Root = Tk()
Root.title(sys.argv[0])
Root.config(bg="light green")
Root.protocol("WM_DELETE_WINDOW", Root.quit)

Value=IntVar()
H_Scale = Scale(Root, label="Pick a number",
                fg="Brown", bg="light blue",
                font=("Helvetica", 24, "bold"),
                variable=Value,
                orient="horizontal",
                length=800,
                from_=-100, to=+100,
                tickinterval=25, resolution=1)
H_Scale.pack(side=TOP, expand=YES, fill=BOTH)

Quit_Button = My_Button()
Quit_Button.config(text="Quit", command=Quit)

State_Button = My_Button()
State_Button.config(text="State", command=Print_Selection)

Root.mainloop()
