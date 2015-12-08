#!/usr/bin/env python

from Tkinter import *
from tkMessageBox import askokcancel
import sys, os

# A simple slider widget and example usage.
# More detail: http://infohost.nmt.edu/tcc/help/pubs/tkinter/scale.html

Root = Tk()
Root.title(sys.argv[0])

def OnSliderValueChanged(value):
	# The value is passes as a string (don't ask why it just is)
	# But you can easily convert to the appropriate value
	lbl.config(text="Slider moved to %f" % (float(value),))
	
def OnButtonClick():
	# Accessing the variable always produces the proper value and type
	lbl.config(text="Slider is at %f" % (SlideVar.get(),))
	
	
def OnResetClick():
	# The slider does not invoke any events when its variable is set
	# so if you want to cause an "slide" event when setting the value
	# you need to use the widgets set() function
	H_Scale.set(0)
	
# A slider control uses an DoubleVar or IntVar to store its values
# DoubleVar and IntVar are similar to StringVar in usage and behavior
SlideVar=DoubleVar()

H_Scale = Scale(Root,
                variable=SlideVar,			
                orient="horizontal",
                length=500,
				from_=0.0,				# can be int or float
                to=1.0,			
                tickinterval=0.1,		# The major intervals
				resolution=0.01,		# The change between two values
				showvalue=False,		
				command=OnSliderValueChanged) # Command invoked when value changes
				
H_Scale.pack(side=TOP, expand=False, fill=X)

btn = Button(Root, text="Report Value", command=OnButtonClick)
btn.pack(side=LEFT)
 
resetBtn = Button(Root, text="Reset", command=OnResetClick)
resetBtn.pack(side=LEFT)

lbl = Label(Root, text="Slide the slider.")
lbl.pack(side=LEFT, expand=False, fill=X)

Root.mainloop()
sys.exit(0)

