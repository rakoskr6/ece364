#! /usr/bin/env python

#     $Author: ee364 $
#       $Date: 2001/10/26 16:30:05 $
#   $Revision: 1.1 $

# The script tries to keep the button to the Left side of
# the window when expanded and fill in Y direction
# The expand option is on

# NOTE: Fill in Y does occur but the label moves to the center

from Tkinter import *
import sys

Root = Tk()
Root.title(sys.argv[0])

My_Label = Label(Root, text = '1I: Hello EE 364 Students',
                       fg="Blue", # foreground color
                       bg="light yellow", # background color
                       font=("courier", 24, "bold"))
My_Label.pack(side=LEFT, expand=YES, fill=Y)
Root.mainloop()

