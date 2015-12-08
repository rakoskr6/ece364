#!/usr/bin/env python

from Tkinter import *
import tkMessageBox
import sys, os

# You will often want to have a confirmation popup when a user closes a window.
# By default closing the root window immediatly terminates the event loop and destroys
# all open windows. You can "hook into" this event with some special bindings

def on_window_delete():
	
	# WARNING! BUG BUG BUG
	# If you are using the default Mac OS X 10.6 Tk/Tcl installation then the window will be deleted
	# no matter what you do. See http://bugs.python.org/issue12584 for details.
	
	# Prompt the user to Quit
	# askokcancel() returns true if the "Yes" option is selected
	if tkMessageBox.askokcancel("Really Quit?", "Do you really want to quit?"):
	        root.quit()

root = Tk()
root.title("Root Window")

# When the root window is closed the on_window_delete function will be called
root.protocol("WM_DELETE_WINDOW", on_window_delete)

for i in range(3):
	w = Toplevel()
	w.title("- Window %d - " % (i, ))
	
	# Similarly, toplevel windows can invoke the same handler
	# This enables any application window closure to cause the application to quit
	w.protocol("WM_DELETE_WINDOW", on_window_delete)
	
root.mainloop()
sys.exit(0)
