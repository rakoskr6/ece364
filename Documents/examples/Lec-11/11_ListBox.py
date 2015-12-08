#! /usr/bin/env python

from Tkinter import *
import sys, os, glob

# Our widgets are in a module
from CustomWidgets import *


def OnDoubleClick(event):
	# Create a document with the selected file
	filename = List.get(ACTIVE)
	doc = DocumentWindow(filename)
		
Root = Tk()

# Create horizontal and vertical scrollbars
HS_Bar = Scrollbar(Root, orient=HORIZONTAL)
HS_Bar.pack(side=BOTTOM, fill=X)

VS_Bar = Scrollbar(Root)
VS_Bar.pack(side=RIGHT, fill=Y)

# Create a list box with scroll commands
List = Listbox(Root, yscrollcommand=VS_Bar.set, xscrollcommand=HS_Bar.set)
List.pack(side=LEFT, expand=YES, fill=BOTH)

# When the widget is double clicked call OnDoubleClick
List.bind("<Double-1>", OnDoubleClick)

HS_Bar.config(command=List.xview)
VS_Bar.config(command=List.yview)

# Get the list of files in the current directory and add them to the list   
for Item in glob.glob("*.py"):
	List.insert(END, Item)

Root.mainloop()

