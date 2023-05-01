from pybricks.hubs import EV3Brick
import pybricks.ev3devices as devices
from pybricks.parameters import Port, Direction
import math

class Bot:

    def __init__(self, name: str, leader: bool):
        
        self.name = name
        self.leader = bool

        self.ir_front = devices.InfraredSensor(Port.S1)
        self.ir_back = devices.InfraredSensor(Port.S2)

    def move_distance(self, delta_x : float, delta_y : float, speed: int):

        theta = math.round(math.degrees(math.atan(delta_y/delta_x)))

        delta_p = math.sqrt(delta_x**2 + delta_y**2)

        self.move_theta(self, delta_p, theta, speed)

    def move_theta(self, delta_p : float, theta : float, speed : int):

        pass

    def get_ball_pos(self):

        pos_front = self.ir_front.distance()
        pos_back = self.ir_back.distance()

        delta = pos_back-pos_front

        try:
            
            return delta/abs(delta)
        
        except ZeroDivisionError:

            return 0
