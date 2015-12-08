#     $Author: ee364 $
#       $Date: 2001/11/02 19:48:40 $
#   $Revision: 1.1 $

from Tkinter import *

class My_Button(Button):
    def __init__(Self, Master=None, **config):
        Button.__init__(Self, Master, config)
        Self.pack(side=LEFT, anchor=NW, expand=YES, fill=BOTH)
        Self.config(text="????", command=Self.Forgot_Command,
            fg="blue", bg="light blue",
            font=("Helvetica", 24, "bold"),
            activeforeground="red",
            activebackground="yellow",
            cursor="dot")
    def Forgot_Command(Self):
        print "Does nothing. No command passed"
