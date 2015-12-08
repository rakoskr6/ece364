#! /usr/bin/env python

#     $Author: ee364 $
#       $Date: 2001/10/26 16:30:05 $
#   $Revision: 1.1 $

# The script keeps the button in the TOP LEFT of
# the window when expanded 
# The button is anchored to the NW (North West) corner
# Fill both X and Y 
# Expand option is off 

from Tkinter import *
import sys

Root = Tk()
Root.title(sys.argv[0])

My_Label = Label(Root, text = '1O: Hello EE 364 Students',
                       fg="Black", # foreground color
                       bg="Blue", # background color
                       font=("Helvetica", 24, "normal"))
My_Label.pack(anchor=NW, expand=YES, fill=BOTH) 
Root.mainloop()
