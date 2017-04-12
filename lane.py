from Tkinter import *
import constants as c
from car import Car
from light import Light

class Lane():
    def __init__(self, initial_x, direction, is_last):
        self.x = initial_x
        self.direction = direction
        self.is_last = is_last
        self.width = c.LANE_WIDTH+c.DOTTED_LINE_WIDTH
        if self.is_last:
            self.width -= +c.DOTTED_LINE_WIDTH
        
        self.light = 0
        self.light_pos = 0
        
    def create_light(self):
        if self.light == 0:
            self.light_pos = c.LIGHT_POSITION
            self.light = Light(self.x, self.light_pos, self.width)

    def get_light_position(self):
        return self.light_pos

    def turn_light_red(self):
        self.light.stop()

    def turn_light_green(self):
        self.light.go()

    def is_light_green(self):
        return self.light.is_green()

    def cancel_light(self):
        if self.light != 0:
            self.light.cancel_timer()
            
    def has_light(self):
        return self.light != 0

    def get_start_position(self):
        return self.x
    
    def get_end_position(self):
        return self.x + self.width

    def get_car_x(self):
        return self.x + (self.width - c.CAR_WIDTH)/2

    def get_direction(self):
        return self.direction

    def draw(self, canvas):
        canvas.create_rectangle(self.x, 0, self.x+self.width, \
                c.HEIGHT, outline=c.COLOR_STREET_GRAY, fill=c.COLOR_STREET_GRAY)
        if (not self.is_last):
            middle_pos = self.x + self.width
            canvas.create_line(middle_pos, 0, middle_pos, c.HEIGHT, fill=c.COLOR_WHITE, width=c.DOTTED_LINE_WIDTH, dash=(40,40))
        
        if (self.light != 0):
            self.light.draw(canvas)

