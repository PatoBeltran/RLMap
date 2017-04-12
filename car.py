import constants as c
from random import randint

COLORS = ["#1abc9c", "#2ecc71", "#3498db", "#9b59b6", "#34495e", "#f1c40f", "#e67e22", "#e74c3c"]

class Car():
    def __init__(self, color, lane, speed, position):
	self.color = color
	self.lane = lane
	self.speed = speed
        self.position = position

    @staticmethod
    def create_new_car(lane, speed):
        return create_new_car_at_position(lane, speed, 0)

    @staticmethod
    def create_new_car_at_position(lane, speed, pos):
        return Car(COLORS[randint(0,7)], lane, speed, pos)

    def change_lanes(self, new_lane):
        self.lane = new_lane
    
    def calculate_position(self):
        direct = self.lane.get_direction()
        if direct == c.DIRECTION_DOWN:
            return self.position
        else:
            pos = 0
            if self.position == 0:
                pos = c.HEIGHT
            else:
                pos = (-1 * (self.position - c.HEIGHT)%c.HEIGHT)
            return pos - c.CAR_HEIGHT

    def update(self):
        self.position = (self.position + self.speed) % c.HEIGHT

    def draw(self, canvas):
        y = self.calculate_position()
        x = self.lane.get_car_x()
        # print 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + ', and color is ' + self.color
        canvas.create_rectangle(x, y, x + c.CAR_WIDTH, y + c.CAR_HEIGHT, fill=self.color, outline=c.COLOR_BLACK)
