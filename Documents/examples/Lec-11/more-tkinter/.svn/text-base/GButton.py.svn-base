#! /usr/bin/env python
#     $Author: ee364 $
#       $Date: 2001/11/02 19:48:40 $
#   $Revision: 1.1 $

from Tkinter import *

class My_Button(Button):
    def __init__(Self, BNum, Master=None, **config):
        Button.__init__(Self, Master, config)
	Self.ID = BNum
        Self.pack(side=LEFT, anchor=NW, expand=YES, fill=BOTH)
        Self.config(text="????", command=Self.Clicked_Button,
            fg="blue", bg="light blue",
            font=("Helvetica", 24, "bold"),
            activeforeground="red",
            activebackground="yellow",
            cursor="dot")
    def Clicked_Button(Self):
        print "Button Number", Self.ID, "Clicked"

root = Tk()

for I in range(0, 10):
  Button = My_Button(I, root)

root.mainloop()
