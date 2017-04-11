import constants as c
from random import randint

class Pedestrian():
    def __init__(self, street, position, direction, speed):
        self.street = street
        self.y = position
        self.direction = direction
        self.x = street.get_starting_for_direction(direction)
        self.speed = speed

    @staticmethod
    def create_random(street):
        return Pedestrian(street, randint(100,c.HEIGHT-100), \
                randint(c.DIRECTION_LEFT, c.DIRECTION_RIGHT), \
                randint(c.PEDESTRIAN_MIN_SPEED, c.PEDESTRIAN_MAX_SPEED))
    
    def has_finished_crossing(self):
        if self.direction == c.DIRECTION_LEFT:
            return self.x > self.street.get_ending_for_direction(self.direction)
        else:
            return self.x < self.street.get_ending_for_direction(self.direction)

    def update(self):
        if self.direction == c.DIRECTION_LEFT:
            self.x = (self.x + self.speed)
        else:
            self.x = (self.x - self.speed)

    def draw(self, canvas):
        canvas.create_oval(self.x, self.y, self.x + c.PEDESTRIAN_DIAMETER, self.y + c.PEDESTRIAN_DIAMETER, fill=c.COLOR_BLUE)
        

