#! /usr/bin/env python

from Tkinter import *
import math
import tkSimpleDialog

class Player:
    def __init__(self, model):
        self.Model = model

        self.Name   = StringVar()
        self.Color  = StringVar()
        self.Angle  = DoubleVar()
        self.Power  = DoubleVar()
        self.Score  = IntVar()

        self.Name.set("<Unknown>")
        self.Color.set("blue")
        self.Angle.set(45.0)
        self.Power.set(50.0)
        self.Score.set(0)
        
        # call self.Model.Changed() when these variables are set
        self.Name.trace('w', lambda *args: self.Model.Changed())
        self.Color.trace('w', lambda *args: self.Model.Changed())
        self.Angle.trace('w', lambda *args: self.Model.Changed())
        self.Power.trace('w', lambda *args: self.Model.Changed())
        self.Score.trace('w', lambda *args: self.Model.Changed())

class Model:
    def __init__(self):
        self.Players = [ Player(self), Player(self) ]
        self.Views = []
        self.Turn = 0       # Index of whose turn it is
        self.Firing = 0     # > 0 when animating a shot

    def RegisterView(self, view):
        """Views must have an OnChange member function"""
        self.Views.append(view)

    def Changed(self):
        """Called to notify the model that something has been changed.
        Generally called automatically by the Player class"""
        for view in self.Views:
            view.OnChange()
    
    def Fire(self):
        self.Firing = True
        angle = self.Players[self.Turn].Angle.get() * math.pi / 180.0 # in rads
        power = self.Players[self.Turn].Power.get()
        vy0 = -power*math.sin(angle)
        vx0 =  power*math.cos(angle)
        # Coefficients to draw the parabola Ax^2 + Bx
        self.A = 0.3/(2*vx0)
        self.B = vy0/vx0
        self.Range = -self.B/self.A
        self.Changed()

    def DoneFiring(self, hit):
        self.Firing = 0
        turn = self.Turn
        if self.Turn == 0:
            self.Turn = 1
        else:
            self.Turn = 0
        if hit:
            s = self.Players[turn].Score.get()
            self.Players[turn].Score.set(s + 1) # This calls Changed()
        else:
            self.Changed()
    
class ControlPanel(Frame):
    def __init__(self, parent, model, player):
        Frame.__init__(self, parent)
        self.Model = model
        self.Player = self.Model.Players[player]

        self.PlayerName = Label(self, textvariable=self.Player.Name)
        self.PlayerName.bind("<Double-Button-1>", self.ChangeName)
        self.PlayerName.grid(row=0, column=0, columnspan=2)

        self.ColorChooser = Frame(self)
        self.ColorChooser.grid(row=1, column=0, columnspan=2)
        self.Red = Radiobutton(self.ColorChooser,
                               text="Red", 
                               variable=self.Player.Color,
                               value = "red")
        self.Red.pack(side=LEFT)
        self.Green = Radiobutton(self.ColorChooser,
                                 text="Green", 
                                 variable=self.Player.Color,
                                 value = "green")
        self.Green.pack(side=LEFT)
        self.Blue = Radiobutton(self.ColorChooser,
                                text="Blue", 
                                variable=self.Player.Color,
                                value = "blue")
        self.Blue.pack(side=LEFT)

        Label(self, text="Angle").grid(row=2, column=0)
        self.AngleScale = Scale(self, 
                                from_=0, 
                                to=90, 
                                showvalue=True,
                                variable=self.Player.Angle,
                                orient=HORIZONTAL)
        self.AngleScale.grid(row=2, column=1)

        Label(self, text="Power").grid(row=3, column=0)
        self.PowerScale = Scale(self, 
                                from_=0, 
                                to=100, 
                                showvalue=True,
                                variable=self.Player.Power,
                                orient=HORIZONTAL)
        self.PowerScale.grid(row=3, column=1)

        self.Score = Label(self, textvariable=self.Player.Score)
        self.Score.grid(row=4, column=0, columnspan=2)
    
        self.FireButton = Button(self, text="Fire", fg="red",
                command = self.OnFire)
        self.FireButton.grid(row=5, column=0, columnspan=2, sticky=E+W)
        self.Model.RegisterView(self)
        self.OnChange() # Called to set up the button properly

    def OnChange(self):
        # This function just greys out the fire button at the right time
        if self.Model.Firing:
            self.FireButton.config(state=DISABLED)
        elif self.Model.Players[self.Model.Turn] is self.Player:
            self.FireButton.config(state=NORMAL)
        else:
            self.FireButton.config(state=DISABLED)
        
    def OnFire(self):
        self.Model.Fire()

    def ChangeName(self, event):
        name = tkSimpleDialog.askstring(title="Change name",
                                        prompt="Enter a new name")        
        if name:
            self.Player.Name.set(name)

class Graphics(Canvas):
    def __init__(self, parent, model):
        Canvas.__init__(self, parent, width=500, height=500, bg="light blue")
        self.Model = model
        self.Model.RegisterView(self)
        # Draw the initial setup
        self.OnChange()

    def OnChange(self):
        # Redraw everything.  Draw back to front

        # Clear the canvas
        self.delete(self.find_all())

        # Draw the sky
        self.create_rectangle(0, 0, 500, 300, fill="light blue",outline="")

        # If it's firing, draw the arc.
        hit = False
        if self.Model.Firing:
            if self.Model.Range >= 370 and self.Model.Range <= 400:
                hit = True
            else:
                hit = False

            if self.Model.Turn == 0:
                x0 = 60
                vx = 1
            else:
                x0 = 440
                vx = -1

            for x in range(int(self.Model.Range)):
                self.create_line(vx*x + x0, 
                        self.Model.A*x**2 + self.Model.B*x + 300, 
                        vx*(x + 1) + x0,
                        self.Model.A*(x+1)**2 + self.Model.B*(x+1) + 300)
            self.after(1000, lambda h=hit : self.Model.DoneFiring(h))

        # Draw player one at (50, 300)
        color = self.Model.Players[0].Color.get()
        angle = self.Model.Players[0].Angle.get()*math.pi/180.0 # in radians
        self.create_line(60, 300, 
                         60+25*math.cos(angle), 300+25*math.sin(-angle),
                         fill=color, width=10)
        self.create_arc((50, 290, 70, 310), fill=color, extent=180.0)

        # Draw player two at (450, 300)
        color = self.Model.Players[1].Color.get()
        angle = self.Model.Players[1].Angle.get()*math.pi/180.0 # in radians
        self.create_line(440, 300, 
                         440-25*math.cos(angle), 300+25*math.sin(-angle),
                         fill=color, width=10)
        self.create_arc((430, 290, 450, 310), fill=color, extent=180.0)


        # Draw the ground at y=300
        self.create_rectangle((0,300,500,500), fill="dark green", outline="")

        # Draw a boom if needed
        if hit:
            if self.Model.Turn == 0:
                self.create_oval(420, 280, 460, 320, fill="red")
            else:
                self.create_oval(40, 280, 80, 320, fill="red")
            
class Game(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Tank battle!")
        self.Model = Model()

        self.LPanel = ControlPanel(self, self.Model, 0)
        self.Graphics = Graphics(self, self.Model)
        self.RPanel = ControlPanel(self, self.Model, 1)

        self.LPanel.grid(row=0, column=0, sticky=N)
        self.Graphics.grid(row=0, column=1, sticky=N+S+E+W)
        self.RPanel.grid(row=0, column=2, sticky=N)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

app = Game()
app.mainloop()
