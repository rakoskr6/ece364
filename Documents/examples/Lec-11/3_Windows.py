#! /usr/bin/env python

from Tkinter import *
import sys, os

# Notice that if you close the root window all Toplevel windows will also close
# But closing a Toplevel does not 
Root = Tk()
Root.title("Root Window")
Root_Label = Label(Root, text = "   This is on the Root window   ") 
Root_Label.pack(side=TOP, expand=YES, fill=BOTH)

# A new (non-root) window is created using the Toplevel class
# Each window may contain its own set of widgets
# you do not assign a parent widget to the Toplevel widget
Window_2 = Toplevel()
Window_2.title("Window 2")
Window_2_Label = Label(Window_2, text = "   This is on window 2   ") 
Window_2_Label.pack(side=TOP, expand=YES, fill=BOTH)

# There can be an arbitrary number of top level windows
Window_3 = Toplevel()
Window_3.title("Window 3")
Window_3_Label = Label(Window_3, text = "   This is on window 3   ") 
Window_3_Label.pack(side=TOP, expand=YES, fill=BOTH)

Root.mainloop()
