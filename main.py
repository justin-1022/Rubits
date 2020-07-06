from CmU_112_GrApHiCs import *
from tkinter import *
from header import *
from Shape import *

class Walker(App):
    def appStarted(self):
        self.the_shape = Shape()

    def keyPressed(self, event):
        if event.key == "d":
            self.the_shape.rotate('r')

        elif event.key == "w":
            self.the_shape.rotate('u')

        elif event.key == "a":
            self.the_shape.rotate('l')

        elif event.key == "s":
            self.the_shape.rotate('d')

    def redrawAll(self, canvas):
        canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill=paintcan.toHex(paintcan.silver))
        canvas.create_text(WIDTH/2, 25, font=('Sans', 20),
                text="Use 'w', 'a', 's', 'd' to control the object.")

        self.the_shape.draw(canvas)

Walker(width=WIDTH, height=HEIGHT)
