#! /usr/bin/env python

from Tkinter import *
import tkMessageBox

# This program demonstates how to scroll widgets on a window.  There is no
# direct way to do this.  Instead we use some of the callbacks associated
# with Scrollbar widgets and repack all the child widgets as needed.

class ScrolledWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Scrolled widgets')

        # Make 100 buttons
        self.Buttons = []
        for i in range(100):
            self.Buttons.append(Button(self, text='Button #%d' % i,
                            command=lambda i=i : self.OnClickButton(i)))

        # Make the first 5 visible initially, and setup grid
        for i in range(5):
            self.rowconfigure(i, weight=1)
            self.Buttons[i].grid(row=i, column=0, sticky=N+S+E+W)
        self.columnconfigure(0, weight=1)

        # Make the scrollbar
        self.Scroll = Scrollbar(self, command=self.OnScroll)
        # Set the scrollbar tab to go from 0% to 5% of the scrollbar
        self.Scroll.set(0.0, 0.05)       # This is required.  Don't omit it
        self.Scroll.grid(row=0, column=1, rowspan=5, sticky=N+S+W)

        # Where we are
        self.StartIndex = 0

    def OnClickButton(self, i):
        tkMessageBox.showinfo('Clicked a button', 'You clicked button #%d' % i)

    def OnScroll(self, method, value, type=None):
        if method=='scroll':    # User clicked on the scroll bar
            # value = '1' or '-1' depending on direction
            # type = 'units' if the user clicked on the arrows
            #        'pages' if the user clicked inside the scrollbar
            if type == 'units':
                self.StartIndex += int(value)
            elif type == 'pages':
                self.StartIndex += 5*int(value)

            if self.StartIndex < 0:
                self.StartIndex = 0
            elif self.StartIndex > len(self.Buttons) - 5:
                self.StartIndex = len(self.Buttons) - 5

        # method = 'moveto' when the user drags the tab somewhere.  Value
        # will contain a string such as 0.01811 or 0.9988 specifying where
        # to move.  type will not be present.

        # Redisplay everything
        for b in self.Buttons:
            b.grid_forget()
        for i in range(5):
            self.Buttons[i + self.StartIndex].grid(row=i, column=0,
                    sticky=N+S+E+W)

        # Reposition the tab.  Each button is 1% of the total range, and the
        # tab should be 5% wide
        self.Scroll.set(self.StartIndex*0.01, self.StartIndex*0.01+0.05)

root = ScrolledWindow()
root.mainloop()
