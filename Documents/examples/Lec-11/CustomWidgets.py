#!/usr/bin/env python

from Tkinter import *
import tkMessageBox
import sys, os

# TK widgets are classes so you can inherit your own widgets with custom functionality
# In this example a class ScrolledText encapsulates the UI from 5_ScrollBars.py
class ScrolledText(Frame):
	def __init__(self, root):
		Frame.__init__(self, root)
		
		self.columnconfigure(0, weight=1)
		self.rowconfigure(0, weight=1)
	
		# Text widget is in (0,0) and should expand to fit its contents
		# Text wrapping is disabled to show horizontal scrolbar support
		self.text = Text(self, background='yellow', foreground='black', wrap=NONE)
		self.text.grid(row=0, column=0, sticky=N+S+E+W)

		# Horizontal scroll bar is in (1,0) and should expand horizontally to fit its contents
		self.hscroll = Scrollbar(self, orient=HORIZONTAL, command=self.text.xview)
		self.hscroll.grid(row=1, column=0, sticky=E+W)

		# Vertical scroll bar is in (0, 1) and should expand vertically to fit its contents
		self.vscroll = Scrollbar(self, orient=VERTICAL, command=self.text.yview)
		self.vscroll.grid(row=0, column=1, sticky=N+S)

		# The text widget must have its scroll commands triger updates to the scrollbar positions
		# Scrollbars have a set(...) member function that changes to position of the scroll bar
		# When the text widget is scrolled it invokes its yscrollcommand or xscrollcommand which 
		# in turn invokes the functions vscroll.set or hscroll.set
		self.text.config(yscrollcommand=self.vscroll.set)
		self.text.config(xscrollcommand=self.hscroll.set)


	def load_text(self, filename):
		# Custom functions provide additional functionality to widgets
		fp = open(filename, "r")
		for line in fp:
			self.text.insert(END, line)
		fp.close()

	def save_text(self, filename):
		fp = open(filename, "w")
		fp.write(self.text.get(1.0,END))
		fp.close()

	def clear_text(self):		
		self.text.delete(1.0, END)

# A toplevel window containing a scrolled text widget
class DocumentWindow(Toplevel):
	def __init__(self, filename):
		Toplevel.__init__(self)
		self.title(filename)
		self.text = ScrolledText(self)
		self.text.pack()
		self.text.load_text(filename)

# This widget will contain a single Label and Entry box (a common UI element)
class LabledEntry(Frame):
	def __init__(self, root):
		Frame.__init__(self, root)

		self.textVar = StringVar()
		self.labelVar = StringVar()

		self.label = Label(self, textvariable=self.labelVar)
		self.label.pack(side=LEFT)

		self.entry = Entry(self, textvariable=self.textVar)
		self.entry.pack(side=LEFT, fill=X, expand=True)

	def get(self):
		return self.textVar.get()

	def set(self, text):
		self.textVar.set(text)

	def set_label(self, text):
		self.labelVar.set(text)

	def get_label(self):
		return self.labelVar.get()
