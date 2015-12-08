#! /usr/bin/env python

#     $Author: ee364 $
#       $Date: 2001/10/26 16:30:05 $
#   $Revision: 1.1 $

# Just a single label in the window
# Adding a name to the program

from Tkinter import *
import sys

Root = Tk()
Root.title(sys.argv[0])

My_Label = Label(Root, text = '1B: Hello EE 364 Students')
My_Label.pack()

Root.mainloop()
