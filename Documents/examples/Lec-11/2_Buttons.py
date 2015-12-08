#! /usr/bin/env python

from Tkinter import *
import sys, os

def Print_Message():
    sys.stdout.write("ECE 364 is a great class!\n")


Root = Tk()

# The "command" value of a button is the name of a function to call when the button is clicked
# It can be a member function or regular function
Hi_Button = Button(Root, text="Push Me", command=Print_Message)
Quit_Button = Button(Root, text="QUIT", command=Root.quit)

# Buttons are packed into the root widget aligned to the left side
# Since Hi_Button is packed first it will be the left most widget
Hi_Button.pack(side=LEFT)
Quit_Button.pack(side=LEFT)

Root.mainloop()

sys.exit(0)