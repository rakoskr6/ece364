#! /usr/bin/env python

#     $Author: ee364 $
#       $Date: 2001/10/26 16:27:50 $
#   $Revision: 1.1 $

from Tkinter import *
import sys
import commands
import string


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

    List = Listbox(Top,
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



File_Name = ""
Root = Tk()
Root.protocol("WM_DELETE_WINDOW", Root.quit)

Quit_Button = Button(Root, text="Quit",
                         command=Root.quit)
Quit_Button.pack(side=LEFT, anchor=NW)

File_Button = Button(Root, text="Select A File",
                         command=Select_A_File)
File_Button.pack(side=LEFT, anchor=NW)

Root.mainloop()

