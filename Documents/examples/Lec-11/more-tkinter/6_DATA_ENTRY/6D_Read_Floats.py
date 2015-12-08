#! /usr/bin/env python

#     $Author: ee364 $
#       $Date: 2001/10/26 16:31:36 $
#   $Revision: 1.1 $

from Tkinter import *
import sys
import tkSimpleDialog

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

Root = Tk()
Root.title(sys.argv[0])
Root.config(bg="yellow")


My_Frame = Frame(Root, width=300, height=300, bg="light blue")
My_Frame.pack(side=TOP, expand=YES, fill=BOTH)

Status = Status_Bar(Root)
Status.pack(side=BOTTOM, expand=YES, fill=BOTH)
Data = ""
while Data != 0:
    try:
        Data = tkSimpleDialog.askfloat("Data Input Box", 
                "Type a floating point number\n0 to Stop")
        Status.Clear()
        Status.Set("%s", Data)
    except:
        sys.exit(0)

Root.mainloop()
