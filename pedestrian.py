import constants as c
from random import randint

COLORS = ["#1abc9c", "#2ecc71", "#3498db", "#9b59b6", "#34495e", "#f1c40f", "#e67e22", "#e74c3c"]

class Pedestrian():
    def __init__(self, street, position, direction):
        self.street = street
        self.y = position
        self.direction = direction
        self.x = street.get_starting_for_direction(direction)

    @staticmethod
    def create_random_pedestrian(street):
        return Pedestrian(street, randint(100,c.HEIGHT-100), randint(2,3))
    
    def has_finished_crossing(self, street):
        if self.direction == c.DIRECTION_LEFT:
            return self.x > street.get_ending_for_direction(self.direction)
        else:
            return self.x < street.get_ending_for_direction(self.direction)

    def update(self):
        if self.direction == c.DIRECTION_LEFT:
            self.x = (self.x + c.PEDESTRIAN_SPEED)
        else:
            self.x = (self.x - c.PEDESTRIAN_SPEED)

    def draw(self, canvas):
        canvas.create_oval(self.x, self.y, self.x+c.PEDESTRIAN_DIAMETER, self.y + c.PEDESTRIAN_DIAMETER, fill=c.COLOR_BLUE)
        
