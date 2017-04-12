from Tkinter import *
import constants as c
from street import Street
from threading import Timer
from car import Car
from pedestrian import Pedestrian
from random import randint
import time

class Environment():
    def __init__(self, master):
        self.master = master
        self.master.title("UT Street Map")
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        street_w = (c.LANE_WIDTH+c.DOTTED_LINE_WIDTH)*c.LANES_PER_STREET - c.DOTTED_LINE_WIDTH + c.STREET_MIDDLE_WIDTH
        self.width = c.NUMBER_OF_STREETS * street_w - c.STREET_MIDDLE_WIDTH;
        
        self.canvas = Canvas(self.master, width = self.width, height = c.HEIGHT, bg = c.COLOR_WHITE)
        self.canvas.pack()

        self.t = 0
        self.t_s = 0
        self.t_p = 0
        self.cars = []
        self.pedestrians = []
        self.streets = []

        for i in range(0, c.NUMBER_OF_STREETS):
            self.streets.append(Street(i*street_w, (c.DIRECTION_DOWN if i < c.NUMBER_OF_STREETS/2 else c.DIRECTION_UP), i == c.NUMBER_OF_STREETS-1))

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
        canvas.delete("all")
        for i in range(0, c.NUMBER_OF_STREETS):
            self.streets[i].draw(self.canvas)
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
        self.t = Timer(1, self._move)
        self.t.start()
    
    def random_stop(self):
        self.t_s = Timer(randint(0, c.RANDOM_STOP_MAX), self._stop_random_street)
        self.t_s.start()

    def random_pedestrian(self):
        self.t_p = Timer(randint(0, c.RANDOM_PEDESTRIAN_MAX), self._create_random_pedestrian)
        self.t_p.start()

    def _stop_random_street(self):
        strt = self.streets[randint(0,c.NUMBER_OF_STREETS-1)]
        if (strt.is_light_green()):
            strt.turn_light_red()
        self.random_stop()

    def _populate_with_cars(self):
        for street in self.streets:
            lanes = street.get_lanes()
            i = 0
            for lane in lanes:
                car_pos = 0
                
                if (i%2 == 0):
                    car_pos = randint(50, c.LIGHT_POSITION-100)
                else:
                    car_pos = randint(c.LIGHT_POSITION+100, c.HEIGHT-50)

                self.cars.append(Car.create_new_car_at_position(lane,0,car_pos))
                i += 1

    def _create_random_pedestrian(self):
        if (len(self.pedestrians) <= c.LIMIT_OF_PEDESTRIANS):
            strt = self.streets[randint(0,c.NUMBER_OF_STREETS-1)]
            self.pedestrians.append(Pedestrian.create_random(strt))
        self.random_pedestrian()

    def on_closing(self):
        if self.t != 0: self.t.cancel() 
        if self.t_s != 0: self.t_s.cancel() 
        if self.t_p != 0: self.t_p.cancel() 
        for strt in self.streets:
            strt.cancel_light()
        self.master.destroy()
            



