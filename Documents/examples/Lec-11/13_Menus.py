#! /usr/bin/env python

from Tkinter import *
from CustomWidgets import *
import tkSimpleDialog, tkMessageBox, tkFileDialog
import sys, os

def donothing():
   pass

def OnNew():
   text.clear_text()
   root.title("New Document")

def OnOpen():
   fname = tkFileDialog.askopenfilename()
   if fname:
      try:
         text.load_text(fname)
         root.title(fname)
      except:
         tkMessageBox.showerror("Error", "Can not open %s" % (fname,))

def OnSave():   
   fname = tkFileDialog.asksaveasfilename()
   try:
      text.save_text(fname)
   except:
      tkMessageBox.showerror("Error", "Can not save to %s" % (fname,))

def OnClose():
   text.clear_text()
   root.title("")

root = Tk()

# WARNING! BUG BUG BUG
# If you are using the default Mac OS X 10.6 Tk/Tcl installation then the menu will not appear!
# For now you should only try this example on the ecelinux machines in lab.

# A menu widget contains other menu widgets to for a set of menues the user can select
# Each menu can have commands, separators and other sub-menus
menubar = Menu(root)

# A sub-menu is just another menu widget
filemenu = Menu(menubar)

# A command is for the most part just like a button
# The specified command callback is run when the menu item is selected
filemenu.add_command(label="New", command=OnNew)
filemenu.add_command(label="Open", command=OnOpen)
filemenu.add_command(label="Save", command=OnSave)
filemenu.add_command(label="Close", command=OnClose)

# A separator is a line that separates menu items
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

# Adding a cascade puts the sub-menu in to the menu bar item
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

# The menu option specifies the menu widget for the main window
root.config(menu=menubar)

text = ScrolledText(root)
text.pack(side=TOP, fill=BOTH, expand=True)

root.mainloop()

sys.exit(0)

