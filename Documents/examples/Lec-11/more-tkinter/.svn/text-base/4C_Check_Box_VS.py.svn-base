#! /usr/bin/env python

#     $Author: ee364 $
#       $Date: 2001/11/02 19:48:40 $
#   $Revision: 1.1 $

from Tkinter import *
from Buttons import *
from Check_Box_V import *
from tkMessageBox import askokcancel
import sys


def Quit():
    Reply = askokcancel("Verify exit",
             "Really want to quit?")
    if Reply != 0:
        Root.destroy()

def EE_364_Response():
    if EE_364_CB.Var.get() == 1:
       print "EE 364 is too easy!"
    else:
       print "Hey it's a good class"
       
def EE_368_Response():
    if EE_368_CB.Var.get() == 1:
       print "EE 368 is the best!"
    else:
       print "Data structures and algorithms!"
       
def EE_264_Response():
    if EE_264_CB.Var.get() == 1:
       print "EE 264 need more homework !"
    else:
       print "Should be in Python not C"
       
def EE_461_Response():
    if EE_461_CB.Var.get() == 1:
       print "EE 461 Game is Yali!"
    else:
       print "Go Software Engineering!"
       
def Print_State():
    print "EE 264: ", EE_264_CB.Var.get()
    print "EE 364: ", EE_364_CB.Var.get()
    print "EE 368: ", EE_368_CB.Var.get()
    print "EE 461: ", EE_461_CB.Var.get()

Root = Tk()
Root.title(sys.argv[0])
Root.config(bg="light green")
Root.protocol("WM_DELETE_WINDOW", Root.quit)

Header = Label(Root, fg="white", bg="blue",
           text="Which classes do you like?",
           font=("Helvetica", 24))
Header.pack(side=TOP, expand=YES, fill=BOTH)

EE_264_CB = Check_Box_V(Root, "EE 264", EE_264_Response)
EE_364_CB = Check_Box_V(Root, "EE 364", EE_364_Response)
EE_364_CB.Var.set(1)
EE_368_CB = Check_Box_V(Root, "EE 368", EE_368_Response)
EE_461_CB = Check_Box_V(Root, "EE 461", EE_461_Response, "disabled")
EE_461_CB.Var.set(1)

Quit_Button = My_Button()
Quit_Button.config(text="Quit", command=Quit)

State_Button = My_Button()
State_Button.config(text="State", command=Print_State)

Root.mainloop()
