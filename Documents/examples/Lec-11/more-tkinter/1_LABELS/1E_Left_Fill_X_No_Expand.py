#! /usr/bin/env python

#     $Author: ee364 $
#       $Date: 2001/10/26 16:30:05 $
#   $Revision: 1.1 $

# The script keeps the button on the left side of 
# the window when expanded and fills in x direction
# No expand option

# NOTE: Fill does not occur

from Tkinter import *
import sys

Root = Tk()
Root.title(sys.argv[0])

My_Label = Label(Root, text = '1E: Hello EE 364 Students',
                       fg="Blue", # foreground color
                       bg="Red", # background color
                       font=("courier", 24, "bold"))
My_Label.pack(side=LEFT, fill=X)
Root.mainloop()
