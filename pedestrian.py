import constants as c
from random import randint

class Pedestrian():
    def __init__(self, position, direction, speed, start, end):
        self.y = position
        self.direction = direction
        self.speed = speed
        self.x = start 
        self.end = end
        self.has_finished = False

    @staticmethod
    def create_random(start, end):
        direction = c.DIRECTION_LEFT if start <= end else c.DIRECTION_RIGHT
        return Pedestrian(randint(100,c.HEIGHT-100), \
                direction, \
                randint(c.PEDESTRIAN_MIN_SPEED, c.PEDESTRIAN_MAX_SPEED),
                start, end)
    
    def is_in_lane(self, lane):
        return lane.get_start_position() <= self.x and lane.get_end_position() >= self.x
    
    def has_finished_crossing(self):
        return self.has_finished

    def get_position(self):
        return self.y
    
    def get_x(self):
        return self.x

    def get_direction(self):
        return self.direction
    
    def update(self):
        if (not self.has_finished):
            if self.direction == c.DIRECTION_LEFT:
                self.x = (self.x + self.speed)
                if self.x > self.end: self.has_finished = True
            else:
                self.x = (self.x - self.speed)
                if self.x < self.end: self.has_finished = True

    def draw(self, canvas):
        canvas.create_oval(self.x, self.y, self.x + c.PEDESTRIAN_DIAMETER, self.y + c.PEDESTRIAN_DIAMETER, fill=c.PEDESTRIAN_COLOR)

