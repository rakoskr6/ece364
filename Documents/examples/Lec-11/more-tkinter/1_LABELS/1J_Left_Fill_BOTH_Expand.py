#! /usr/bin/env python

#     $Author: ee364 $
#       $Date: 2001/10/26 16:30:05 $
#   $Revision: 1.1 $

# The script tries to keep the button on the left side of
# the window when expanded and fill in both X and Y directions.
# Expand option is on.

# Note:  Expands in both X an Y directions. Label is centered

from Tkinter import *
import sys

Root = Tk()
Root.title(sys.argv[0])

My_Label = Label(Root, text = '1J: Hello EE 364 Students',
                       fg="Red", # foreground color
                       bg="Blue", # background color
                       font=("courier", 24, "bold"))
My_Label.pack(side=LEFT, expand=YES, fill=BOTH)
Root.mainloop()
