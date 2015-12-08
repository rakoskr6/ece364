#     $Author: ee364 $
#       $Date: 2001/11/02 19:48:40 $
#   $Revision: 1.1 $

from Tkinter import *

class Radio_Box_H:
   def __init__(Self, Master,
                Radio_Label,
                Radio_Command,
                Radio_Variable,
                State="normal"):
       Self = Radiobutton(Master,
           text=Radio_Label,
           command=Radio_Command,
           fg="Brown", bg="light green",
           activebackground="yellow",
           activeforeground="Blue",
           disabledforeground="Red",
           font=("Helvetica", 24),
           cursor="plus",
           state=State,
           value=Radio_Label,
           variable=Radio_Variable)
       Self.pack(side=LEFT, expand=YES, fill=BOTH)
