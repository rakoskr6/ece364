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
    for I in range(len(Data_Box)):
        print "%10s: %s" % (Data_Entry_Labels[I], Data_Box[I].get())
        Data_Box[I].delete(0, END)

def Make_Form (Master, Data_Fields = []):
    Data_Items = []
    for Field in Data_Fields:

        Row = Frame(Master)
        Row.pack(side=TOP, fill=X)

        Row_Label = Label(Row, width=5, text=Field,
                      fg="Red", bg="light blue",
                      font=('courier', 24, "bold"))
        Row_Label.pack(side=LEFT) 

        Row_Entry = Entry(Row, fg="Black", bg="light green",
                      font=("Helvetica", 24),
                      cursor="X_cursor")                     
        Row_Entry.pack(side=RIGHT, expand=YES, fill=X)
	Row_Entry.insert(0, "TEST")
	
        Data_Items.append(Row_Entry)
    return Data_Items

Data_Entry_Labels = ["Name", "Age", "Phone"]

Root = Tk()
Root.title(sys.argv[0])
Root.config(bg="light green")
Root.protocol("WM_DELETE_WINDOW", Root.quit)

Data_Box=Make_Form(Root, Data_Entry_Labels)

Quit_Button = My_Button()
Quit_Button.config(text="Quit", command=Quit)


Fetch_Button = My_Button()
Fetch_Button.config(text="FETCH THE DATA",
         command=Fetch_Data)
Fetch_Button.config(bg="orange")

Root.mainloop()
