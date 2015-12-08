#     $Author: ee364 $
#       $Date: 2001/11/02 19:48:40 $
#   $Revision: 1.1 $

from Tkinter import *

class Check_Box_H:
   def __init__(Self, Master,
                Check_Label,
                Check_Command,
                State="normal"):
       Self.Var=IntVar()
       Self = Checkbutton(Master,
           text=Check_Label,
           command=Check_Command,
           fg="Brown", bg="light green",
           activebackground="yellow",
           activeforeground="Blue",
           disabledforeground="Red",
           font=("Helvetica", 24),
           cursor="plus",
           state=State,
           variable=Self.Var)
       Self.pack(side=LEFT, expand=YES, fill=BOTH)
