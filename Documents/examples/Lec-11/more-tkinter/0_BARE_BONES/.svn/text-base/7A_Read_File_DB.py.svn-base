#! /usr/bin/env python

#     $Author: ee364 $
#       $Date: 2001/10/26 16:27:50 $
#   $Revision: 1.1 $

from Tkinter import *
import sys
import tkSimpleDialog
import tkMessageBox

class Status_Bar(Frame):
    def __init__ (Self, Master):
        Frame.__init__(Self, Master)
        Self.label = Label(Self, width=40,
            font = ("Courier", 24, "bold"),
            justify=LEFT)
        Self.label.pack(fill=X)

    def Set(Self, Format, *args):
        Self.label.config(text=Format % args)
        Self.label.update_idletasks()

    def Clear(Self):
        Self.label.config(text="")
        Self.label.update_idletasks()


Root = Tk()
Root.protocol("WM_DELETE_WINDOW", sys.exit)


Quit_Button = Button(Root, text="Quit",
                         command=Root.quit);
Quit_Button.pack(side=TOP)

Status = Status_Bar(Root)
Status.pack(side=BOTTOM, fill=X)

File_Name = ""
Number_Of_Trys = 0

File_Read = 0
while (     (Number_Of_Trys < 3) \
        and (File_Read == 0)):
    Number_Of_Trys += 1
    Message = "You have 3 tries\nto enter a file name" \
               + "\nThis is try # " + str(Number_Of_Trys)
    try:
        File_Name = tkSimpleDialog.askstring(
           "Get a File Name: Try # %d" % Number_Of_Trys,
            Message)
    except:
        sys.exit()

    try:
        FP = open(File_Name)
    except:
        tkMessageBox.showwarning(
            "Open file",
            "File: %s could not be opened\n" % File_Name)
        File_Name = ""
    else:
        File_Info = ""
        Line = FP.readline()
        while Line != "":
            File_Info = File_Info + Line
            Line =FP.readline()
        FP.close()
        File_Read = 1
        try:
            Status.Clear()
            Status.Set("%s", File_Info)
        except:
            sys.exit(0)

Root.mainloop()
