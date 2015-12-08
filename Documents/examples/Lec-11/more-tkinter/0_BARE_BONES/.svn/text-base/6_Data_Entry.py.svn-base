#! /usr/bin/env python

#     $Author: ee364 $
#       $Date: 2001/10/26 16:27:50 $
#   $Revision: 1.1 $

from Tkinter import *
import sys
import tkSimpleDialog

class Status_Bar(Frame):
    def __init__ (Self, Master):
        Frame.__init__(Self, Master)
        Self.label = Label(Self, width=40)
        Self.label.pack(fill=X)

    def Set(Self, Format, *args):
        Self.label.config(text=Format % args)
        Self.label.update_idletasks()

    def Clear(Self):
        Self.label.config(text="")
        Self.label.update_idletasks()

Root = Tk()

Status = Status_Bar(Root)
Status.pack(side=BOTTOM, expand=YES, fill=BOTH)

Data = ""
while Data != "Quit":
    try:
        Data = tkSimpleDialog.askstring("Text Input Box", 
                "Type Anything\nQuit to Stop")
        Status.Clear()
        Status.Set("%s", Data)
    except:
        sys.exit(0)

Root.mainloop()
