from Tkinter import *
import constants as c
from street import Street
from threading import Timer
import time

class Environment():
    def __init__(self, master):
        master.title("UT Street Map")
        street_w = (c.LANE_WIDTH+c.DOTTED_LINE_WIDTH)*c.LANES_PER_STREET - c.DOTTED_LINE_WIDTH + c.STREET_MIDDLE_WIDTH
        self.width = c.NUMBER_OF_STREETS * street_w - c.STREET_MIDDLE_WIDTH;
        
        self.canvas = Canvas(master, width = self.width, height = c.HEIGHT, bg = c.COLOR_WHITE)
        self.canvas.pack()

        self.streets = []
        for i in range(0, c.NUMBER_OF_STREETS):
            self.streets.append(Street(i*street_w, (c.DIRECTION_DOWN if i < c.NUMBER_OF_STREETS/2 else c.DIRECTION_UP), i == c.NUMBER_OF_STREETS-1))

        self.draw(self.canvas)
        
        self.start_movement()

    def update(self):
        for strt in self.streets:
            strt.update()

    def draw(self, canvas):
        canvas.delete("all")
        for i in range(0, c.NUMBER_OF_STREETS):
            self.streets[i].draw(self.canvas)

    def _move(self):
        self.update()
        self.draw(self.canvas)
        self.canvas.after(100)
        self.start_movement()
            
    def start_movement(self):
        t = Timer(1, self._move)
        t.start()

