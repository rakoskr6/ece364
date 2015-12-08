#! /usr/bin/env python

#     $Author: ee364 $
#       $Date: 2001/10/26 16:26:55 $
#   $Revision: 1.1 $

from Tkinter import *
import sys
import commands
import string

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
            fg="black", bg="light blue",
            font= ("courier", 22, "bold"),
            relief=SUNKEN, wrap=NONE)
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


def Handle_List_Extraction(event):
    global File_Name
    Index = Top.Selection_List.curselection()
    File_Name = Top.Selection_List.get(Index)
    Top.destroy()
  
def Select_A_File():
    global Top

    Top = Toplevel()

    HS_Bar = Scrollbar(Top, orient=HORIZONTAL)
    HS_Bar.pack(side=BOTTOM, fill=X)

    VS_Bar = Scrollbar(Top)
    VS_Bar.pack(side=RIGHT, fill=Y)

    List = Listbox(Top, relief=SUNKEN,
                  font=("courier", 22, "bold"),
                  fg="Red", bg="light blue",
                  selectforeground="blue",
                  selectbackground="white",
                  cursor="arrow",
                  yscrollcommand=VS_Bar.set,
                  xscrollcommand=HS_Bar.set)

    HS_Bar.config(command=List.xview)
    VS_Bar.config(command=List.yview)
    List.pack(side=LEFT, expand=YES, fill=BOTH)

    Entries=commands.getoutput("ls *.py")
    Entries=string.split(Entries,"\n")
    for Item in Entries:
            List.insert(END, Item)
    Top.Selection_List = List

    List.bind("<Double-1>", Handle_List_Extraction)

    Top.focus_set()
    Top.grab_set()
    Top.wait_window()
    print "File selected: %s" % (File_Name)
    Read_File(File_Name)


def Read_File(File_Name):
    try:
        File_Text = open(File_Name, "r").read()
    except:
        tkMessageBox.showwarning("Open file",
              "File: %s could not be opened\n" % File_Name)
        File_Name = ""
        File_Text = ""
    
    try:
       File_Window.destroy()
    except:
       pass

    File_Window = Toplevel()
    File_Window.title(File_Name)
    File_Window.config(bg="yellow")
    File_Window.config(cursor="gobbler")
    File_Window.protocol("WM_DELETE_WINDOW", File_Window.destroy)
    ST = Scrolled_Text(File_Window, File_Text)
    

File_Name = ""
Root = Tk()
Root.title(sys.argv[0])
Root.config(bg="yellow")
Root.config(cursor="gobbler")
Root.protocol("WM_DELETE_WINDOW", Root.quit)

Quit_Button = Button(Root, text="Quit",
                         fg="Red", bg="light blue",
                         activeforeground="light blue",
                         activebackground="Red",
                         font=("Helvedica", 24),
                         cursor="X_cursor",
                         command=Root.quit)
Quit_Button.pack(side=LEFT)

File_Button = Button(Root, text="Select A File",
                         fg="Blue", bg="light blue",
                         activeforeground="light blue",
                         activebackground="Blue",
                         font=("Helvedica", 24),
                         cursor="dot",
                         command=Select_A_File)
File_Button.pack(side=LEFT)

Root.mainloop()

