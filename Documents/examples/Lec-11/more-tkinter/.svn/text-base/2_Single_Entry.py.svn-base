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

def Fetch_Data():
    print "Data Entered was: %s" % (Data_Box.get())
    Data_Box.delete(0, END)

 
Root = Tk()
Root.title(sys.argv[0])
Root.config(bg="light green")
Root.protocol("WM_DELETE_WINDOW", Root.quit)

Data_Label=Label(Root, text="Enter some text",
                 font=("Helvetica", 24),
                 fg="White", bg="green")
Data_Label.pack(side=TOP, fill=X)
Data_Box = Entry(Root, fg="blue", bg="light blue",
                 cursor="X_cursor",
                 font=("Helvetica", 24))
Data_Box.insert(0, "")
Data_Box.pack(side=TOP, fill=X)
Quit_Button = My_Button()
Quit_Button.config(text="Quit", command=Quit)


Fetch_Button = My_Button()
Fetch_Button.config(text="FETCH THE DATA", command=Fetch_Data)
Fetch_Button.config(bg="orange")

Root.mainloop()
