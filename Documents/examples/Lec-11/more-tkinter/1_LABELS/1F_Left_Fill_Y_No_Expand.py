#! /usr/bin/env python

#     $Author: ee364 $
#       $Date: 2001/10/26 16:30:05 $
#   $Revision: 1.1 $

# The script keeps the button to the Left side of
# the window when expanded and fills in Y direction
# No expand option

# NOTE: Fill in Y does occur

from Tkinter import *
import sys

Root = Tk()
Root.title(sys.argv[0])

My_Label = Label(Root, text = '1F: Hello EE 364 Students',
                       fg="Blue", # foreground color
                       bg="light blue", # background color
                       font=("courier", 24, "bold"))
My_Label.pack(side=LEFT, fill=Y)
Root.mainloop()

