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
                 fg="red", bg="Blue",
                 activeforeground="blue",
                 activebackground="red",
                 font=("Times", 20, "bold"),
                 relief=RAISED, bd=5,
                 command=Root.quit)
Quit_Button.pack(side=BOTTOM)

Hi_Button = Button(Root,
                 text="2C: Whatever",
                 fg="blue", bg="white",
                 activeforeground="white",
                 activebackground="blue",
                 font=("Helvetica", 30),
                 relief=RIDGE, bd=5,
                 command=Print_Message)
Hi_Button.pack(side=TOP)

Root.mainloop()
