#!/usr/bin/env python
# encoding: utf-8

from Tkinter import *
import tkMessageBox
import sys, os

# Our widgets are in a module
from CustomWidgets import *

def on_return(event):
	# The event.widget field is a reference to the widget that generated the event
	# This is useful if we do not have direct access to or do not know what widget caused
	# the event
	tkMessageBox.showwarning("Return Event Handled!", "Message: %s" % (event.widget.get(),))
	
	
root = Tk()
root.title(sys.argv[0])

for i in range(0,13):
	# Create the widget
	e = LabledEntry(root)
	e.set_label("Field %d: " % (i, ))
	e.entry.bind("<Return>", on_return)
	
	# Arrange the widgets in a grid with upto 5 per column
	e.grid(row=(i%5), column=(i/5), sticky=E+W)
	
	# Ensure any used columns are set to expand with an equal weight
	root.columnconfigure((i/5), weight=1)
	
root.mainloop()
sys.exit(0)
