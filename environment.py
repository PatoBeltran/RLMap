from Tkinter import *
import constants as c
from street import Street

class Environment():
    def __init__(self, master):
        master.title("UT Street Map")
        street_w = (c.LANE_WIDTH+c.DOTTED_LINE_WIDTH)*c.LANES_PER_STREET - c.DOTTED_LINE_WIDTH + c.STREET_MIDDLE_WIDTH
        self.width = c.NUMBER_OF_STREETS * street_w - c.STREET_MIDDLE_WIDTH;
        
        self.canvas = Canvas(master, width = self.width, height = c.HEIGHT, bg = c.COLOR_WHITE)
        self.canvas.pack()

        self.streets = []
        for i in range(0, c.NUMBER_OF_STREETS):
            self.streets.append(Street(i*street_w, (c.DIRECTION_DOWN if i < c.NUMBER_OF_STREETS/2 else c.DIRECTION_UP), i == c.NUMBER_OF_STREETS-1))

        self.draw(self.canvas)
        
        # self.start_movement()

    def draw(self, canvas):
        canvas.delete("all")
        for i in range(0, c.NUMBER_OF_STREETS):
            self.streets[i].draw(self.canvas)


    # def _move(self):
        # w = self.rectWidth
        # while True:
            # lock = threading.Lock()
            # lock.acquire()
            # endRect = self.rectangles.pop()
            # frontCoords = self.canvas.coords(self.rectangles[0])
            # endCoords = self.canvas.coords(endRect)
            # #(Below for Debugging)
            # #print self.direction
            # #print "Front: " + str(frontCoords) + " Back: " + str(endCoords)
            # if self.direction == "left":
                # self.canvas.move(self.canvas.gettags(endRect), int(frontCoords[0]-endCoords[0])-w,\
                                 # int(frontCoords[1]-endCoords[1]))
            # elif self.direction == "down":
                # self.canvas.move(self.canvas.gettags(endRect), int(frontCoords[0]-endCoords[0]),\
                                 # int(frontCoords[1]-endCoords[1])+w)
            # elif self.direction == "right":
                # self.canvas.move(self.canvas.gettags(endRect), int(frontCoords[0]-endCoords[0])+w,\
                                 # int(frontCoords[1]-endCoords[1]))
            # elif self.direction == "up":
                # self.canvas.move(self.canvas.gettags(endRect), int(frontCoords[0]-endCoords[0]),\
                                 # int(frontCoords[1]-endCoords[1])-w)
            # self.canvas.after(100)
            # self.rectangles.insert(0, endRect)
            # lock.release()
            # self.check_bounds()
            # self.check_collide()

    # def start_movement(self):
        # threading.Thread(target=self._move).start()

