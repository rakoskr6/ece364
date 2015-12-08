#! /usr/bin/env python

#     $Author: ee364 $
#       $Date: 2001/10/26 16:27:50 $
#   $Revision: 1.1 $

from Tkinter import *
import sys
import tkSimpleDialog
import tkMessageBox
import tkFileDialog

class Scrolled_Text(Frame):
    def __init__ (Self, Master=None,
                  Text="", File=None):
        Frame.__init__(Self, Master)
        Self.Make_Widgets()
        Self.Set_Text(Text, File)
        Self.pack(expand=YES, fill=BOTH)

    def Make_Widgets(Self):
        VS_Bar = Scrollbar(Self)
        VS_Bar.pack(side=RIGHT, fill=Y)

        HS_Bar = Scrollbar(Self, orient="horizontal")
        HS_Bar.pack(side=BOTTOM, fill=X)

        Some_Text = Text(Self,
            width=40, height=20,
            wrap=NONE)
        Some_Text.pack(side=TOP, expand=YES, fill=BOTH)

        VS_Bar.config(command=Some_Text.yview)
        HS_Bar.config(command=Some_Text.xview)

        Some_Text.config(xscrollcommand=HS_Bar.set)
        Some_Text.config(yscrollcommand=VS_Bar.set)

        Self.Text = Some_Text

    def Set_Text(Self, Text="", File=None):
        if File:
            Text = open(File, "r").read()
        Self.Text.delete('1.0', END)
        Self.Text.insert('1.0', Text)
        Self.Text.mark_set(INSERT, '1.0')
        Self.Text.focus()

    def Get_Text(Self):
        return Self.Text.get('1.0', END+'-1c')

Root = Tk()


File_Name=""
while File_Name == "":
    File_Name = tkFileDialog.askopenfilename()
  
    try:
        File_Text = open(File_Name, "r").read()
    except:
        tkMessageBox.showwarning("Open file",
              "File: %s could not be opened\n" % File_Name)
        File_Name = ""
        File_Text = ""

    ST = Scrolled_Text(Text=File_Text)
     
Root.mainloop()
