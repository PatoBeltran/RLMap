from Tkinter import *
import constants as c
from threading import Timer
from car import Car
from lane import Lane
from pedestrian import Pedestrian
from random import randint
import time

class Environment():
    def __init__(self, master):
        self.master = master
        self.master.title("UT Street Map")
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        lane_w = c.LANE_WIDTH+c.DOTTED_LINE_WIDTH
        self.width = (lane_w)*c.LANES - c.DOTTED_LINE_WIDTH
        
        self.canvas = Canvas(self.master, width = self.width, height = c.HEIGHT, bg = c.COLOR_WHITE)
        self.canvas.pack()

        self.t = 0
        self.t_s = 0
        self.t_p = 0
        self.cars = []
        self.pedestrians = []
        self.lanes = []
        self.closing = False

        for i in range(0, c.LANES):
            self.lanes.append(Lane(i*lane_w, (c.DIRECTION_DOWN if i < c.LANES/2 else c.DIRECTION_UP), i == c.LANES-1))

        for lane in self.lanes:
            lane.create_light()
        
        self._populate_with_cars()
        self.draw(self.canvas)
        self.start_movement()
        self.random_stop()
        self.random_pedestrian()

    def update(self):
        for pedestrian in self.pedestrians:
            pedestrian.update()
        for car in self.cars:
            car.update()
        self.pedestrians = filter(lambda ped: not ped.has_finished_crossing(), self.pedestrians)

    def draw(self, canvas):
        if not self.closing:
            canvas.delete("all")
            for lane in self.lanes:
                lane.draw(canvas)
            for car in self.cars:
                car.draw(canvas)
            for pedestrian in self.pedestrians:
                pedestrian.draw(canvas)

    def _move(self):
        self.update()
        self.draw(self.canvas)
        self.canvas.after(100)
        self.start_movement()
            
    def start_movement(self):
        self.t = Timer(0.1, self._move)
        self.t.start()
    
    def random_stop(self):
        self.t_s = Timer(randint(0, c.RANDOM_STOP_MAX), self._stop_random_lane)
        self.t_s.start()

    def random_pedestrian(self):
        self.t_p = Timer(randint(0, c.RANDOM_PEDESTRIAN_MAX), self._create_random_pedestrian)
        self.t_p.start()

    def _stop_random_lane(self):
        lane = self.lanes[randint(0,c.LANES-1)]
        if (lane.has_light() and lane.is_light_green()):
            lane.turn_light_red()
        self.random_stop()

    def _populate_with_cars(self):
        i = 0
        for lane in self.lanes:
            car_pos = 0
            
            if (i%2 == 0):
                car_pos = randint(50, c.LIGHT_POSITION-100)
            else:
                car_pos = randint(c.LIGHT_POSITION+100, c.HEIGHT-50)

            self.cars.append(Car.create_new_car_at_position(lane, 10, car_pos))
            i += 1

    def _create_random_pedestrian(self):
        if (len(self.pedestrians) <= c.LIMIT_OF_PEDESTRIANS):
            rand = randint(0, 1)
            ped = 0
            if rand == 0:
                ped = Pedestrian.create_random(0, self.width)
            else:
               ped = Pedestrian.create_random(self.width, 0)
            self.pedestrians.append(ped)

        self.random_pedestrian()

    def on_closing(self):
        self.closing = True
        if self.t != 0: self.t.cancel() 
        if self.t_s != 0: self.t_s.cancel() 
        if self.t_p != 0: self.t_p.cancel() 
        for lane in self.lanes:
            lane.cancel_light()
        self.master.destroy()
            



