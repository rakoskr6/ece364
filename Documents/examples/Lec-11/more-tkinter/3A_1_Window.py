#! /usr/bin/env python

#     $Author: ee364 $
#       $Date: 2001/10/26 16:26:55 $
#   $Revision: 1.1 $

from Tkinter import *
import sys

Root = Tk()
Root.title(sys.argv[0])

Script = Label(Root, text = "This is on the Root window", 
                font=("Helvetica", 24, "bold"),
                justify=CENTER,
                bg="Light green", fg="Black")
Script.pack(side=TOP, expand=YES, fill=BOTH)

Root.mainloop()
