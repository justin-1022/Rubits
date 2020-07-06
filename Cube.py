import copy
from tkinter import *
from header import *

class Cube():
    #note - these can be changed to anything, temp values for now

    #rubucks cube
    def __init__(self):
        #[front, right, back, left, top, bottom]
        self.state = [WHITE, RED, YELLOW, ORANGE, BLUE, GREEN]

    def __eq__(self, other):
        if self.state == other.state: return True

    def rotate(self, direction):
        #rotating entire cube
        ns = copy.deepcopy(self.state) #ns = new_state

        if direction == RIGHT:
            ns[0], ns[1], ns[2], ns[3] = ns[1], ns[2], ns[3], ns[0]

        elif direction == UP:
            ns[0], ns[5], ns[2], ns[4] = ns[5], ns[2], ns[4], ns[0]

        else:
            return 1

        self.state = ns
        return 0

    def draw(self, canvas):
        color = self.state[0]

        canvas.create_rectangle(50, 50, 850, 850, fill=paintcan.toHex(self.state[0]))
