#!/usr/bin/env python
# encoding: utf-8

from Tkinter import *
import sys, os

# Our widgets are in a module
from CustomWidgets import *
				
if len(sys.argv) <= 1 or len(sys.argv) > 4:
	sys.stderr.write("usage: 9_CustomWidgets.py <file1> [<file2> <file3>]\n")
	sys.exit(1)		
		
root = Tk()
root.title(sys.argv[0])

# Try to build a scrolled text box for each input file
for filename in sys.argv[1:]:
	try:
		txt = ScrolledText(root)
		txt.text.configure(width=32)
		txt.load_text(filename)
		txt.pack(side=LEFT, expand=True, fill=BOTH)
	except Exception as e:
		sys.stderr.write("error: %s\n" % (e,))

root.mainloop()
sys.exit(0)
