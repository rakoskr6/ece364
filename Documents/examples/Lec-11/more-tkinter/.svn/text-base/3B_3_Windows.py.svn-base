#! /usr/bin/env python

#     $Author: ee364 $
#       $Date: 2001/10/26 16:32:36 $
#   $Revision: 1.1 $

from Tkinter import *
import sys


Root = Tk()
Root.title(sys.argv[0])

Root_Label = Label(Root, text = "This is on the Root window", 
                font=("Helvetica", 24, "bold"),
                justify=CENTER,
                bg="Light green", fg="Black")
Root_Label.pack(side=TOP, expand=YES, fill=BOTH)


Window_2 = Toplevel()
Window_2.title("Window 2")

Window_2_Label = Label(Window_2, text = "This is on window 2", 
                font=("Helvetica", 24, "bold"),
                justify=CENTER,
                bg="Light green", fg="Black")
Window_2_Label.pack(side=TOP, expand=YES, fill=BOTH)

Window_3 = Toplevel()
Window_3.title("Window_3")

Window_3_Label = Label(Window_3, text = "This is on window 3 ", 
                font=("Helvetica", 24, "bold"),
                justify=CENTER,
                bg="Light green", fg="Black")
Window_3_Label.pack(side=TOP, expand=YES, fill=BOTH)

Root.mainloop()
