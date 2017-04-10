from Tkinter import *
import constants as c

class Lane():
    def __init__(self, street, initial_x, is_last):
        self.x = initial_x
        self.width = c.LANE_WIDTH
        self.street = street
        self.is_last = is_last

    def draw(self, canvas):
        canvas.create_rectangle(self.x, 0, self.x+self.width, \
                c.HEIGHT, outline=c.COLOR_STREET_GRAY, fill=c.COLOR_STREET_GRAY)
        if (not self.is_last):
            middle_pos = self.x + self.width + c.DOTTED_LINE_WIDTH/2
            canvas.create_line(middle_pos, 0, middle_pos, c.HEIGHT, fill=c.COLOR_WHITE, width=c.DOTTED_LINE_WIDTH, dash=(40,40))


