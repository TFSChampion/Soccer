from pybricks.hubs import EV3Brick
import pybricks.ev3devices as devices
from pybricks.parameters import Port, Direction
import math

class Bot:

    def __init__(self, name: str, leader: bool):
        
        self.name = name
        self.leader = bool

        self.ir_right = devices.InfraredSensor(Port.S1)
        self.ir_left = devices.InfraredSensor(Port.S2)

    def move_distance(self, delta_x : float, delta_y : float, speed: int):

        theta = math.round(math.degrees(math.atan(delta_y/delta_x)))

        delta_p = math.sqrt(delta_x**2 + delta_y**2)

        self.move_theta(self, delta_p, theta, speed)

    def move_theta(self, delta_p : float, theta : float, speed : int):

        pass

    def get_ball_pos(self):

        d = None

        r_left = self.ir_left.distance()
        r_right = self.r_right.distance()

        theta = 90 - (math.acos((d**2+r_left**2-r_right**2)/(2*d*r_left))*(180/math.pi))

        delta_x = math.sin(theta)*r_left
        delta_y = math.cos(theta)*r_left

        return (delta_x, delta_y)
