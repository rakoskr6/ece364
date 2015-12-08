#! /usr/bin/env python

#     $Author: ee364 $
#       $Date: 2001/11/02 19:48:40 $
#   $Revision: 1.1 $

from Tkinter import *
from Buttons import *
from Radio_Box_V import *
from tkMessageBox import askokcancel
import sys

def Quit():
    Reply = askokcancel("Verify exit",
             "Really want to quit?")
    if Reply != 0:
        Root.destroy()


def EE_364_Response():
       print "EE 364 is too easy!"
       
def EE_368_Response():
       print "EE 368 is the best!"
       
def EE_264_Response():
       print "Should be in Python not C"
       
def EE_461_Response():
       print "EE 461 Game is Yali!"
       
def Print_State():
    print "You Selected", Box_Var.get()

Root = Tk()
Root.title(sys.argv[0])
Root.config(bg="light green")
Root.protocol("WM_DELETE_WINDOW", Root.quit)

Header = Label(Root, fg="white", bg="blue",
           text="Which class do you like best?",
           font=("Helvetica", 24))
Header.pack(side=TOP, expand=YES, fill=BOTH)

Box_Var = StringVar()

EE_264_CB = Radio_Box_V(Root, "EE 264", EE_264_Response, Box_Var)
EE_364_CB = Radio_Box_V(Root, "EE 364", EE_364_Response, Box_Var)
EE_368_CB = Radio_Box_V(Root, "EE 368", EE_368_Response, Box_Var)
EE_461_CB = Radio_Box_V(Root, "EE 461", EE_461_Response, Box_Var)

Quit_Button = My_Button()
Quit_Button.config(text="Quit", command=Quit)

State_Button = My_Button()
State_Button.config(text="State", command=Print_State)

Root.mainloop()
