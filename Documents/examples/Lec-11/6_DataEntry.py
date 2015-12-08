#! /usr/bin/env python

from Tkinter import *
import sys, os

root = Tk()

# This GUI will be organized as follows:
# --------------------------------
# | Entry Selection Entry Button |
# | Label                        |
# --------------------------------
#
# The entry widgets will accept as input two numbers
# The selection widget will allow the user to select an operation
# The label will display a result


# A table of operator -> function mappings
# Lambda functions avoid the need to formally def them
operations = {
	'' : None, # Special "no operation" 
	'+': lambda x,y: x+y,
	'-': lambda x,y: x-y,
	'*': lambda x,y: x*y,
	'/': lambda x,y: x/y,
	'max': lambda x,y: max((x,y)),
	'min': lambda x,y: min((x,y))
}

def DoCalculate():
	# Get the operation to perform see below for use of opVar
	op = operations[opVar.get()]
	
	try:
		# Get the values of the two entry boxes
		A = float(entA.get())
		B = float(entB.get())
		result = op(A, B)
		
	except Exception as e:
		resultVar.set("Error: %s" % (e,))
		
	else:
		resultVar.set("%f %s %f = %f" % (A, opVar.get(), B, result))

# To acieve the above layout without using the grid geometry manager
# two frames will be created and packed into the root widget
topRow = Frame(root)
topRow.pack(side=TOP, expand=False, fill=X)

bottomRow = Frame(root)
bottomRow.pack(side=TOP, expand=False, fill=X)

# Entry widgets are text boxes for inputting data
entA = Entry(topRow)
entA.pack(side=LEFT, expand=False, fill=X)

entB = Entry(topRow)
entB.pack(side=LEFT, expand=False, fill=X)

# The OptionMenu uses a StringVar to maintain the "current" selection
# To get or set the value of the selection use opVar.set(...) or opVar.get()
opVar = StringVar()
opVar.set('')

op = OptionMenu(topRow, opVar, *operations.keys())
op.pack(side=LEFT, expand=False, fill=X)

# Perform the calculation when the button is clicked
btn = Button(topRow, text='Calculate', command=DoCalculate)
btn.pack(side=LEFT, expand=False, fill=X)

# A label will display the result stored in the StringVar resultVar
resultVar = StringVar()
resultVar.set('Perform an operation.')

lbl = Label(bottomRow, textvariable=resultVar)
lbl.pack(side=LEFT, expand=False, fill=X)

root.mainloop()
sys.exit(0)