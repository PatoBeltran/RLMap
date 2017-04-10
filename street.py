from Tkinter import *
import constants as c
from lane import Lane

class Street():
    def __init__(self, initial_x, direction, is_last):
        self.x = initial_x
        self.direction = direction
        self.is_last = is_last
        self.width = (c.LANE_WIDTH+c.DOTTED_LINE_WIDTH)*c.LANES_PER_STREET - c.DOTTED_LINE_WIDTH
        self.lanes = []
        for i in range(0, c.LANES_PER_STREET):
            self.lanes.append(Lane(self, initial_x + i*(c.LANE_WIDTH+c.DOTTED_LINE_WIDTH), i == c.LANES_PER_STREET - 1))
    
    def draw(self, canvas):
        canvas.create_rectangle(self.x, 0, self.x+self.width, c.HEIGHT, fill=c.COLOR_STREET_GRAY)
        if (not self.is_last):
            middle_pos = self.x + self.width + c.STREET_MIDDLE_WIDTH/2
            canvas.create_line(middle_pos, 0, middle_pos, c.HEIGHT, fill=c.COLOR_YELLOW, width=c.STREET_MIDDLE_WIDTH)
        for i in range(0, c.LANES_PER_STREET):
            self.lanes[i].draw(canvas)


