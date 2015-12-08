#! /usr/bin/env python

#     $Author: ee364 $
#       $Date: 2001/10/26 16:26:55 $
#   $Revision: 1.1 $

from Tkinter import *
import commands
import sys

Root = Tk()
Root.title(sys.argv[0])
Root.config(bg="light green")

def Call_Back():
    print "You called Me!"

def Get_Listing():
    Listing = commands.getoutput("ls -last .")
    print Listing
    
# Generate a toolbar

Tool_Bar = Frame(Root, cursor="gobbler", bg="Orange")

B_1 = Button(Tool_Bar, text="Hey you!",
          fg="Red", bg="light blue",
          activeforeground="green",
          activebackground="red",
          font = ("Times", 30),
          cursor="pirate",
          command=Call_Back)
B_1.pack(side=LEFT, padx=5, pady=5)

B_2 = Button(Tool_Bar, text="Get directory listing",
          fg = "white", bg = "blue",
          activeforeground="blue",
          activebackground="yellow",
          font = ("Helvetica", 40, "bold"),
          cursor="spider",
          command=Get_Listing)
B_2.pack(side=LEFT, padx=5, pady=5)

Tool_Bar.pack(side=TOP, fill=X)

Root.mainloop()
