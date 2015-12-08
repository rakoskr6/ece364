#! /usr/bin/env python

#     $Author: ee364 $
#       $Date: 2001/11/06 16:43:31 $
#   $Revision: 1.2 $

from Tkinter import *
import sys

def Print_Message():
    print "Its a great class!"

Root = Tk()
Root.title(sys.argv[0])
Root.config(bg="yellow")
Root.config(cursor="gobbler")

Quit_Button = Button(Root, text="QUIT",
                  fg="white", bg="Blue",
                  activeforeground="blue",
                  activebackground="red",
                  font=("Times", 20, "bold"),
                  relief=RAISED, bd=5,
                  cursor="iron_cross",
                  command=Root.quit)
Quit_Button.pack(side=BOTTOM)

Hi_Button = Button(Root, text="2D: Whatever",
                  fg="Black", bg="orange",
                  activeforeground="yellow",
                  activebackground="light blue",
                  font=("Helvetica", 30),
                  relief=RIDGE, bd=5,
                  cursor="dot",
                  command=Print_Message)
Hi_Button.pack(side=TOP)

Root.mainloop()
