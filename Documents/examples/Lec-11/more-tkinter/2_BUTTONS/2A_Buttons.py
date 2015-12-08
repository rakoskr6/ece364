#! /usr/bin/env python

#     $Author: ee364 $
#       $Date: 2001/10/26 16:29:01 $
#   $Revision: 1.1 $

# A couple of buttons in a window

from Tkinter import *
import sys

def Print_Message():
    print "EE 364 is a great class!"


Root = Tk()
Root.title(sys.argv[0])

Quit_Button = Button(Root, text="QUIT",
                command=Root.quit)
Quit_Button.pack(side=LEFT)

Hi_Button = Button(Root, text="2A: Push me",
                command=Print_Message)
Hi_Button.pack(side=LEFT)

Root.mainloop()
