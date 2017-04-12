from Tkinter import *
import constants as c
from threading import Timer
from random import randint

class Light():
    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width
        self.light_on = c.GREEN_LIGHT
        self.t = 0        

    def _change_light(self, new_light):
        self.light_on = new_light

    def _set_red(self):
        self._change_light(c.RED_LIGHT)
        self.t = Timer(randint(c.YELLOW_LIGHT_DURATION, c.YELLOW_LIGHT_DURATION+10), self._set_green)
        self.t.start()

    def _set_green(self):
        self._change_light(c.GREEN_LIGHT)
        self.t = 0

    def stop(self):
        self._change_light(c.YELLOW_LIGHT)
        self.t = Timer(c.YELLOW_LIGHT_DURATION, self._set_red)
        self.t.start()

    def go(self):
        self.cancel_timer()
        self._change_light(c.GREEN_LIGHT)

    def cancel_timer(self):
        if (self.t != 0):
            self.t.cancel()
            self.t = 0

    def is_green(self):
        return self.light_on == c.GREEN_LIGHT

    def is_yellow(self):
        return self.light_on == c.YELLOW_LIGHT
    
    def draw(self, canvas):
        green_color = c.COLOR_BLACK
        yellow_color = c.COLOR_BLACK
        red_color = c.COLOR_BLACK

        if self.light_on == c.GREEN_LIGHT:
            green_color = c.COLOR_GREEN
        elif self.light_on == c.RED_LIGHT:
            red_color = c.COLOR_RED
        else:
            yellow_color = c.COLOR_YELLOW


        lights_width = (c.LIGHT_RADIUS*2 + c.LIGHT_MARGIN*2)*3;
        lights_margin = (self.width - lights_width)/2

        green_x0 = self.x + lights_margin + c.LIGHT_MARGIN
        green_x1 = self.x + lights_margin + c.LIGHT_RADIUS*2 + c.LIGHT_MARGIN

        yellow_x0 = self.x + lights_margin + c.LIGHT_RADIUS*2 + c.LIGHT_MARGIN*3
        yellow_x1 = self.x + lights_margin + c.LIGHT_RADIUS*4 + c.LIGHT_MARGIN*3

        red_x0 = self.x + lights_margin + c.LIGHT_RADIUS*4 + c.LIGHT_MARGIN*5
        red_x1 = self.x + lights_margin + c.LIGHT_RADIUS*6 + c.LIGHT_MARGIN*5

        canvas.create_rectangle(self.x, self.y, self.x+self.width, self.y+c.LIGHT_HEIGHT, fill=c.COLOR_BLACK)
        canvas.create_oval(green_x0, self.y, green_x1, self.y + c.LIGHT_RADIUS*2, fill=green_color)
        canvas.create_oval(yellow_x0, self.y, yellow_x1, self.y + c.LIGHT_RADIUS*2, fill=yellow_color)
        canvas.create_oval(red_x0, self.y, red_x1, self.y + c.LIGHT_RADIUS*2, fill=red_color)

