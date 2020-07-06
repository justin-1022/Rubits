from CmU_112_GrApHiCs import *
from tkinter import *
from header import *
from Cube import *

class Walker(App):
    def appStarted(self):
        self.the_cube = Cube()

    def keyPressed(self, event):
        if event.key == "d":
            self.the_cube.rotate('r')

        elif event.key == "w":
            self.the_cube.rotate('u')

    def redrawAll(self, canvas):
        canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="grey")

        self.the_cube.draw(canvas)

Walker(width=WIDTH, height=HEIGHT)
