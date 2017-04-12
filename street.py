from Tkinter import *
import constants as c
from lane import Lane
from light import Light
from random import randint

class Street():
    def __init__(self, initial_x, direction, is_last):
        self.x = initial_x
        self.direction = direction
        self.is_last = is_last
        self.width = (c.LANE_WIDTH+c.DOTTED_LINE_WIDTH)*c.LANES_PER_STREET - c.DOTTED_LINE_WIDTH
        self.lanes = []

        for i in range(0, c.LANES_PER_STREET):
            self.lanes.append(Lane(self, initial_x + i*(c.LANE_WIDTH+c.DOTTED_LINE_WIDTH), i == c.LANES_PER_STREET - 1))

        self.light_pos = randint(100, c.HEIGHT-100)
        self.light = Light(self.x, self.light_pos, self.width)
    
    def get_direction(self):
        return self.direction

    def get_light_position(self):
        return self.light_pos
    
    def get_starting_for_direction(self, direction):
        if direction == c.DIRECTION_LEFT:
            return self.x
        else:
            return self.x + self.width

    def get_ending_for_direction(self, direction):
        if direction == c.DIRECTION_LEFT:
            return self.x + self.width
        else:
            return self.x

    def get_random_lane(self):
        return self.lanes[randint(0, c.LANES_PER_STREET - 1)]

    def turn_light_red(self):
        self.light.stop()

    def turn_light_green(self):
        self.light.go()

    def is_light_green(self):
        return self.light.is_green()

    def cancel_light(self):
        self.light.cancel_timer()
        
    def get_lanes(self):
        return self.lanes
    
    def draw(self, canvas):
        canvas.create_rectangle(self.x, 0, self.x+self.width, c.HEIGHT, fill=c.COLOR_STREET_GRAY)
        if (not self.is_last):
            middle_pos = self.x + self.width + c.STREET_MIDDLE_WIDTH/2
            canvas.create_line(middle_pos, 0, middle_pos, c.HEIGHT, fill=c.COLOR_YELLOW, width=c.STREET_MIDDLE_WIDTH)
        
        for lane in self.lanes:
            lane.draw(canvas)

        self.light.draw(canvas)

