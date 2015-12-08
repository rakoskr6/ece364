#! /usr/bin/env python

#     $Author: ee364 $
#       $Date: 2001/10/26 16:29:01 $
#   $Revision: 1.1 $

from Tkinter import *
import sys

def Print_Message():
    print "Its a great class!"

Root = Tk()
Root.title(sys.argv[0])
Root.config(bg="yellow")

Quit_Button = Button(Root, text="QUIT",
                 fg="red", bg="green", bd=2,
                 font=("Times", 20, "bold"),
                 command=Root.quit)
Quit_Button.pack(side=LEFT, anchor=NW)

Hi_Button = Button(Root, text="2B: Hello 364 students",
                 fg="blue", bg="white", bd=4,
                 font=("Helvetica", 30, "italic"),
                 command=Print_Message)
Hi_Button.pack(side=LEFT, anchor=NW)

Root.mainloop()
