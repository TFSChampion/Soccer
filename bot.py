from pybricks.hubs import EV3Brick
import pybricks.ev3devices as devices
from pybricks.parameters import Port, Direction
import math

class Bot:

    def __init__(self, name: str, leader: bool):
        
        self.name = name
        self.leader = bool

    def move_distance(self, delta_x : float, delta_y : float, speed: int):

        theta = math.round(math.degrees(math.atan(delta_y/delta_x)))

        delta_p = math.sqrt(delta_x**2 + delta_y**2)

        self.move_theta(self, delta_p, theta, speed)

    def move_theta(self, delta_p : float, theta : float, speed : int):

        pass