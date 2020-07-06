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

        elif event.key == "a":
            self.the_cube.rotate('l')

        elif event.key == "s":
            self.the_cube.rotate('d')

    def redrawAll(self, canvas):
        canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill=paintcan.toHex(paintcan.silver))
        canvas.create_text(WIDTH/2, 25, font=('Sans', 20),
                text="Press 'd' to rotate right and 'w' to rotate up.")

        self.the_cube.draw(canvas)

Walker(width=WIDTH, height=HEIGHT)
