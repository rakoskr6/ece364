#! /usr/bin/env python

from Tkinter import *
import tkMessageBox
import sys, os, re

# This example shows how to make use of the <Key> event for processing keyboard events

def handle_key_event(event):
	status_message.set("char: %s keycode: %s keysym: %s" % (event.char, event.keycode, event.keysym))

def handle_ent_return(event):
	# Display the message in an alert box
	# See http://effbot.org/tkinterbook/tkinter-standard-dialogs.htm for more detials
	if entBoxVar.get().lower() == "quit":
		Root.quit()
	else:
		tkMessageBox.showwarning("Return Event Handled!", "Message: %s" % (entBoxVar.get(),))
		entBoxVar.set('')

Root = Tk()
Root.title(sys.argv[0])

# You can specify the size of the root window as a string
# Width x Height (in pixels)
# Note: Most widgets have height and width configuration options but
# windows are special and require a separate function call
Root.geometry("%dx%d" % (400, 200))

# A frame is a widget that contains other widgets
Upper_Frame = Frame(Root, background='red')
Upper_Frame.pack(side=TOP, expand=True, fill=BOTH)

# This text box will be placed at the top of the frame and its contents 
# will be held in a string variable
entBoxVar = StringVar()
entBox = Entry(Upper_Frame, textvariable=entBoxVar)
entBox.pack(side=TOP, expand=False, fill=X)
entBox.bind("<Return>", handle_ent_return)

# This frame is positioned at the bottom
Status_Frame = Frame(Root)
Status_Frame.pack(side=BOTTOM, expand=False, fill=X)

# A StringVar is a special variable that contains a String value
# Some Tk widgets can be assigned a StringVar value instead of static text
# This allows the value to be updated dynamically using var.set(...)
status_message = StringVar()
status_message.set('Type a key on your keyboard.')

# Labels can be assigned a StringVar instead of text
My_Label = Label(Status_Frame, textvariable=status_message)
My_Label.pack(side=LEFT, expand=True, fill=X)

# The <Key> event corresponds to a key press on the keyboard
Root.bind("<Key>", handle_key_event)


Root.mainloop()

sys.exit(0)