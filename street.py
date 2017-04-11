from Tkinter import *
import constants as c
from lane import Lane
from car import Car
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

        for i in range(0, c.LANES_PER_STREET):
            self.lanes.append(Lane(self, initial_x + i*(c.LANE_WIDTH+c.DOTTED_LINE_WIDTH), i == c.LANES_PER_STREET - 1))

        self.cars.append(Car.create_new_car(self.lanes[randint(0,1)], 40))
        
        self.light = Light(self.x, randint(100, c.HEIGHT-100), self.width)
    
    def get_direction(self):
        return self.direction

    # def check_collisions(self):


    def update(self):
        for car in self.cars:
            car.update()

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


