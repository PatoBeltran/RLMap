import constants as c
from random import randint
from pedestrian import Pedestrian

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
        return Car(c.COMPUTER_COLOR, lane, speed, pos)

    def change_lanes(self, new_lane):
        self.lane = new_lane
    
    def distance_to_light(self):
        if not self.lane.has_light():
            return -1
        direction = self.lane.get_direction()
        if direction == c.DIRECTION_DOWN:
            if self.position <= c.LIGHT_POSITION:
                return c.LIGHT_POSITION - self.position
            elif self.position >= c.LIGHT_POSITION + c.LIGHT_HEIGHT:
                return self.position - (c.LIGHT_POSITION + c.LIGHT_HEIGHT)
            else:
                return 0
        else:
            if self.position <= c.LIGHT_POSITION - c.LIGHT_HEIGHT:
                return c.LIGHT_POSITION - c.LIGHT_HEIGHT - self.position
            elif self.position >= c.LIGHT_POSITION:
                return self.position - c.LIGHT_POSITION
            else:
                return 0

    def approaching_to_light(self):
        if self.lane.has_light():
            direction = self.lane.get_direction()
            if direction == c.DIRECTION_DOWN and self.position <= c.LIGHT_POSITION:
                return True
            if direction == c.DIRECTION_UP and self.position <= c.LIGHT_POSITION - c.LIGHT_HEIGHT:
                return True
        return False

    def distance_to_pedestrian(self, pedestrian):
        ped_pos = self._calculate_position_in_lane(pedestrian.get_position())
        car_pos = self._calculate_position()

        if car_pos + c.CAR_HEIGHT <= ped_pos:
            return car_pos + c.CAR_HEIGHT - ped_pos
        elif car_pos >= ped_pos + c.PEDESTRIAN_DIAMETER:
            return ped_pos + c.PEDESTRIAN_DIAMETER - car_pos
        else:
            return 0
    
    def approaching_to_pedestrian(self, pedestrian):
        ped_dir = pedestrian.get_direction()
        car_x = self.lane.get_car_x()
        if ped_dir == c.DIRECTION_LEFT:
            return car_x > pedestrian.get_x() + c.PEDESTRIAN_DIAMETER
        else:
            return car_x + c.CAR_WIDTH < pedestrian.get_x()

    def _calculate_position(self):
        return self._calculate_position_in_lane(self.position)

    def _calculate_position_in_lane(self, position):
        if self.lane.get_direction() == c.DIRECTION_DOWN:
            return position
        else:
            pos = 0
            if position == 0:
                pos = c.HEIGHT
            else:
                pos = (-1 * (position - c.HEIGHT)%c.HEIGHT)
            return pos - c.CAR_HEIGHT


    def update(self):
        self.position = (self.position + self.speed) % c.HEIGHT

    def draw(self, canvas):
        y = self._calculate_position()
        x = self.lane.get_car_x()
        canvas.create_rectangle(x, y, x + c.CAR_WIDTH, y + c.CAR_HEIGHT, fill=self.color, outline=c.COLOR_BLACK)
