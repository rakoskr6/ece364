#! /usr/bin/env python

#     $Author: ee364 $
#       $Date: 2001/11/06 00:40:14 $
#   $Revision: 1.2 $

from Tkinter import *
from Buttons import *
import sys


def Quit():
    Root.destroy()

def Hello():
    print "Hello"

Root = Tk()
Root.title(sys.argv[0])
Root.config(bg="light green")
Root.protocol("WM_DELETE_WINDOW", Root.quit)

Quit_Button = My_Button()
Quit_Button.config(text="Quit", command=Quit)

Hello_Button = My_Button()
Hello_Button.config(text="Press me", command=Hello)
Hello_Button.config(bg="orange")
Opps_Button = My_Button()

Whatever_Button = My_Button()
Whatever_Button.config(text="Whatever")

Win = Toplevel()
Win.title("2nd. Window")

Hello_Again = My_Button(Win)
Hello_Again.config(text="Hello Again", command=Hello)

Quit_Win = My_Button(Win)
Quit_Win.config(text="QUIT", command=Win.destroy)
Quit_Win.config(cursor="gobbler", fg="White", bg="green")

Root.mainloop()
