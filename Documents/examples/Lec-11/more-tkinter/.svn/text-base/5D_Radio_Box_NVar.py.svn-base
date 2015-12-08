#! /usr/bin/env python

#     $Author: ee364 $
#       $Date: 2001/11/02 19:48:40 $
#   $Revision: 1.1 $

from Tkinter import *
from Buttons import *

from tkMessageBox import askokcancel
import sys

def Quit():
    Reply = askokcancel("Verify exit",
             "Really want to quit?")
    if Reply != 0:
        Root.destroy()

Button_List = []

def On_Press(I):
    global State
    State = I
    for Button in Button_List:
        Button.deselect()
    Button_List[I].select()

Root = Tk()
Root.title(sys.argv[0])
Root.config(bg="light green")
Root.protocol("WM_DELETE_WINDOW", Root.quit)

Header = Label(Root, fg="white", bg="blue",
           text="Check some boxes",
           font=("Helvetica", 24))
Header.pack(side=TOP, expand=YES, fill=BOTH)

State = ""
for I in range(5):
   Radio_Box = Radiobutton(Root, text=str(I),
               value=str(I),
               fg="Blue", bg="Light Blue",
               font=("Helvetica", 24, "bold"),
               activeforeground="Red",
               activebackground="Yellow",
               cursor="plus",
               command=(lambda I=I: On_Press(I)))
   Radio_Box.pack(side=LEFT, expand=YES, fill=X)
   Button_List.append(Radio_Box)

Quit_Button = My_Button()
Quit_Button.config(text="Quit", command=Quit)


Root.mainloop()
print "Radio_Box button:", State, "selected"

