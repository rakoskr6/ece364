#! /usr/bin/env python

from Tkinter import *

root = Tk()

def Go(num):
  print "You clicked button " + `num`

for BNum in range(0,10):
  Button(root, text="Button"+`BNum`, command=(lambda but=BNum: Go(but))).pack(side=LEFT)

root.mainloop()
