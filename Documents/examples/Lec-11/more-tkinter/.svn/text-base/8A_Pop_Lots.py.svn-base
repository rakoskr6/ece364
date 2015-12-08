#! /usr/bin/env python

from Tkinter import *
import sys
I=0
def Dialog():
    global I
    I = I + 1
 
    Window = Toplevel()
    Window.title(sys.argv[0] + ":" + str(I))
    Label(Window,
       text=("Window: " + str(I) + " Make me go away")).pack()
    Button(Window,
           text="OK",
           command=Window.destroy).pack()
Root = Tk()
Root.title(sys.argv[0])
Button(Root, text="Pop Up A Window",
       command=Dialog).pack()
Root.mainloop()
