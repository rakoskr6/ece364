#! /usr/bin/env python

#     $Author: ee364 $
#       $Date: 2001/10/26 16:26:55 $
#   $Revision: 1.1 $

from Tkinter import *
import sys

import tkSimpleDialog
import tkMessageBox

class Status_Bar(Frame):
    def __init__ (Self, Master):
        Frame.__init__(Self, Master)
        Self.label = Label(Self, bd=1,
            font = ("Courier", 24, "bold"),
            fg="Red", bg="light green",
            justify=LEFT,
            relief=SUNKEN, anchor=W)
        Self.label.pack(fill=X)

    def Set(Self, Format, *args):
        Self.label.config(text=Format % args)
        Self.label.update_idletasks()

    def Clear(Self):
        Self.label.config(text="")
        Self.label.update_idletasks()

def Call_Back(Event):
     global Message
     print "Gumby at", Event.x, Event.y
     Message = "Gumby at X: " + str(Event.x) + ", Y: " + str(Event.y)
     Status.Clear()
     Status.Set("%s", Message) 


Root = Tk()
Root.title(sys.argv[0])


Status = Status_Bar(Root)
Status.pack(side=BOTTOM, fill=X)
Message = ""
My_Frame = Frame(Root, width=400, height=200,
           bg="light blue", cursor="gumby")
My_Frame.bind("<Button-1>", Call_Back)
My_Frame.pack(side=TOP, expand=YES, fill=BOTH)

Root.mainloop()

