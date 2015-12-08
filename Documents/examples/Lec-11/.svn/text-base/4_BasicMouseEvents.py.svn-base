#! /usr/bin/env python

from Tkinter import *
import sys, os

def handle_mouse_event(event):
	# Change the value of the StringVar status_message
	# Observe what happens to the text
	status_message.set("You clicked at (%d, %d)" % (event.x, event.y))
	
def handle_motion_event(event):
	status_message.set("Your mouse is at (%d, %d)" % (event.x, event.y))

Root = Tk()
Root.title(sys.argv[0])

# A frame is a widget that contains other widgets
Upper_Frame = Frame(Root, width=400, height=200, background='blue')
Upper_Frame.pack(side=TOP, expand=True, fill=BOTH)

# This frame is positioned at the bottom
Status_Frame = Frame(Root)
Status_Frame.pack(side=BOTTOM, expand=False, fill=X)

# A StringVar is a special variable that contains a String value
# Some Tk widgets can be assigned a StringVar value instead of static text
# This allows the value to be updated dynamically using var.set(...)
status_message = StringVar()
status_message.set('Click the empty space in the window.')

# Labels can be assigned a StringVar instead of text
My_Label = Label(Status_Frame, textvariable=status_message)
My_Label.pack(side=LEFT, expand=True, fill=X)

# The <Button-1> event corresponds to the left mouse button clicking on the widget
Upper_Frame.bind("<Button-1>", handle_mouse_event)

# The <Motion> event corresponds to the mouse hovering over the widget
Upper_Frame.bind("<Motion>", handle_motion_event)

Root.mainloop()

sys.exit(0)