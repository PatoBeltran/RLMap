from Tkinter import *
import constants as c
from lane import Lane
from car import Car
from pedestrian import Pedestrian
from light import Light
from random import randint

class Street():
    def __init__(self, initial_x, direction, is_last):
        self.x = initial_x
        self.direction = direction
        self.is_last = is_last
        self.width = (c.LANE_WIDTH+c.DOTTED_LINE_WIDTH)*c.LANES_PER_STREET - c.DOTTED_LINE_WIDTH
        self.lanes = []
        self.cars = []
        self.pedestrians = []

        for i in range(0, c.LANES_PER_STREET):
            self.lanes.append(Lane(self, initial_x + i*(c.LANE_WIDTH+c.DOTTED_LINE_WIDTH), i == c.LANES_PER_STREET - 1))

        self.cars.append(Car.create_new_car(self.lanes[randint(0,1)], 40))
        self.pedestrians.append(Pedestrian.create_random(self))
        
        self.light = Light(self.x, randint(100, c.HEIGHT-100), self.width)
    
    def get_direction(self):
        return self.direction

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

    # def check_collisions(self):


    def update(self):
        for car in self.cars:
            car.update()
        for pedestrian in self.pedestrians:
            pedestrian.update()
        self.pedestrians = filter(lambda x: not x.has_finished_crossing(self), self.pedestrians)


    def draw(self, canvas):
        canvas.create_rectangle(self.x, 0, self.x+self.width, c.HEIGHT, fill=c.COLOR_STREET_GRAY)
        if (not self.is_last):
            middle_pos = self.x + self.width + c.STREET_MIDDLE_WIDTH/2
            canvas.create_line(middle_pos, 0, middle_pos, c.HEIGHT, fill=c.COLOR_YELLOW, width=c.STREET_MIDDLE_WIDTH)
        
        for lane in self.lanes:
            lane.draw(canvas)
            
        for car in self.cars:
            car.draw(canvas)

        self.light.draw(canvas)

        for pedestrian in self.pedestrians:
            pedestrian.draw(canvas)


