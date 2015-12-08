#! /usr/bin/env python

#     $Author: ee364 $
#       $Date: 2001/10/26 16:27:50 $
#   $Revision: 1.1 $

from Tkinter import *
import commands
import sys

Root = Tk()

def Call_Back():
    print "You called Me!"

def Get_Listing():
    Listing = commands.getoutput("ls -last .")
    print Listing
    
# Generate a toolbar

Tool_Bar = Frame(Root)

B_1 = Button(Tool_Bar, text="Hey you!",
          command=Call_Back)
B_1.pack(side=LEFT)

B_2 = Button(Tool_Bar, text="Get directory listing",
          command=Get_Listing)
B_2.pack(side=LEFT)

Tool_Bar.pack(side=TOP, fill=X)

Root.mainloop()
