#! /usr/bin/env python

#     $Author: ee364 $
#       $Date: 2001/10/26 16:27:50 $
#   $Revision: 1.1 $

# A couple of buttons in a window

from Tkinter import *

def Print_Message():
    print "EE 364 is a great class!"


Root = Tk()

Quit_Button = Button(Root, text="QUIT",
                     command=Root.quit)
Quit_Button.pack(side=LEFT)
Hi_Button = Button(Root, text="Push Me",
                     command=Print_Message)
Hi_Button.pack(side=LEFT)

Root.mainloop()
