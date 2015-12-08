#! /usr/bin/env python

from Tkinter import *
import sys, os

# This example shows basic use of scroll bars and grid layout

if len(sys.argv) != 2:
	sys.stderr.write("usage: 5_ScrollBars.py <file>\n")
	sys.exit(1)
	
if not os.access(sys.argv[1], os.R_OK) or not os.path.isfile(sys.argv[1]):
	sys.stderr.write("error: %s is not a readable file.\n" % (sys.argv[1],))
	sys.exit(1)


root = Tk()

# Our grid will be arranged into 4 quadrants:
#    0,0 | 0,1
#    ---------
#    1,0 | 1,1
# With the text widget in (0,0), the horizontal scroll bar in (1,0) and the vertical
# scrollbar in (0, 1). The quadrant (1,1) will be empty.

# We want the grid to expand the main text box in (0,0) as the window changes size
# So we will configure the rows and columns to have a non-zero weight
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Text widget is in (0,0) and should expand to fit its contents
# Text wrapping is disabled to show horizontal scrolbar support
txtWidget = Text(root, background='yellow', foreground='black', wrap=NONE)
txtWidget.grid(row=0, column=0, sticky=N+S+E+W)

# Horizontal scroll bar is in (1,0) and should expand horizontally to fit its contents
hscroll = Scrollbar(root, orient=HORIZONTAL, command=txtWidget.xview)
hscroll.grid(row=1, column=0, sticky=E+W)

# Vertical scroll bar is in (0, 1) and should expand vertically to fit its contents
vscroll = Scrollbar(root, orient=VERTICAL, command=txtWidget.yview)
vscroll.grid(row=0, column=1, sticky=N+S)

# The text widget must have its scroll commands triger updates to the scrollbar positions
# Scrollbars have a set(...) member function that changes to position of the scroll bar
# When the text widget is scrolled it invokes its yscrollcommand or xscrollcommand which 
# in turn invokes the functions vscroll.set or hscroll.set
txtWidget.config(yscrollcommand=vscroll.set)
txtWidget.config(xscrollcommand=hscroll.set)


# Load the input file into the text widget:
try:
	fp = open(sys.argv[1], "r")
	for line in fp:
		# insert takes a location and the text
		txtWidget.insert(END, line)
		
finally:
	if fp:	
		fp.close()
		
# Run the program:
root.mainloop()
sys.exit(0)
