#! /usr/bin/env python

#     $Author: ee364 $
#       $Date: 2001/10/26 16:27:50 $
#   $Revision: 1.1 $

from Tkinter import *
import sys

Root = Tk()
Root.title(sys.argv[0])

def Call_Back(Event):
     print "Clicked at", Event.x, Event.y

My_Frame = Frame(Root, width=400, height=200)
My_Frame.bind("<Button-1>", Call_Back)
My_Frame.pack()

Root.mainloop()
