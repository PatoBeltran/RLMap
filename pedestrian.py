import constants as c
from random import randint

class Pedestrian():
    def __init__(self, street, position, direction, speed):
        self.street = street
        self.y = self._calculate_y(position)
        self.direction = direction
        self.x = street.get_starting_for_direction(direction)
        self.speed = speed

    @staticmethod
    def create_random(street):
        return Pedestrian(street, randint(100,c.HEIGHT-100), \
                randint(c.DIRECTION_LEFT, c.DIRECTION_RIGHT), \
                randint(c.PEDESTRIAN_MIN_SPEED, c.PEDESTRIAN_MAX_SPEED))
    
    def is_in_lane(self, street, lane):
        if (self.street != street):
            return False
        return lane.get_start_position() <= self.x and lane.get_end_position() >= self.x
    
    def get_street(self):
        return self.street
    
    def has_finished_crossing(self):
        if self.direction == c.DIRECTION_LEFT:
            return self.x > self.street.get_ending_for_direction(self.direction)
        else:
            return self.x < self.street.get_ending_for_direction(self.direction)

    def _calculate_y(self, posi):
        direct = self.street.get_direction()
        if direct == c.DIRECTION_DOWN:
            return posi
        else:
            pos = 0
            if posi == 0:
                pos = c.HEIGHT
            else:
                pos = (-1 * (posi - c.HEIGHT)%c.HEIGHT)
            return pos - c.PEDESTRIAN_DIAMETER

    def get_position(self):
        return self.y
    
    def get_x(self):
        return self.x

    def get_direction(self):
        return self.direction
    
    def update(self):
        if self.direction == c.DIRECTION_LEFT:
            self.x = (self.x + self.speed)
        else:
            self.x = (self.x - self.speed)

    def draw(self, canvas):
        canvas.create_oval(self.x, self.y, self.x + c.PEDESTRIAN_DIAMETER, self.y + c.PEDESTRIAN_DIAMETER, fill=c.COLOR_BLUE)
        

