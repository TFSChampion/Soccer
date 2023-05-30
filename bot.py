from pybricks.hubs import EV3Brick
import pybricks.ev3devices as devices
from pybricks.parameters import Port
import math

class Bot:

    def __init__(self, goalie : bool):

        self.goalie = goalie

        self.ir_right = devices.InfraredSensor(Port.S1)
        self.ir_left = devices.InfraredSensor(Port.S4)

        if goalie:

            self.mo_front = devices.Motor(Port.A)
            self.mo_back = devices.Motor(Port.B)

        self.mo_right = devices.Motor(Port.C)
        self.mo_left = devices.Motor(Port.D)

    def motor_on_theta(self, theta : float, speed : int):

        if self.goalie:

            raise NotImplementedError("motor_on_theta is not implemented when bot is a goalie.")

        vertical_speed_coef = math.cos(theta)
        horizontal_speed_coef = math.sin(theta)

        self.mo_front.run(int(speed*vertical_speed_coef))
        self.mo_back.run(int(speed*vertical_speed_coef))
        self.mo_right.run(int(speed*horizontal_speed_coef))
        self.mo_left.run(int(speed*horizontal_speed_coef))

    def start_turn(self, clockwise : bool, speed : int):

        self.mo_left.run(speed if clockwise else 0)
        self.mo_right.run(0 if clockwise else speed)

    def get_ball_pos(self):

        d = 100

        relative_distance_left = self.ir_left.distance()
        relative_distance_right = self.ir_right.distance()

        r_left = (relative_distance_left/100)*600
        r_right = (relative_distance_right/100)*600

        theta = 90 - (math.acos((d**2+r_left**2-r_right**2)/(2*d*r_left))*(180/math.pi))

        delta_x = math.sin(theta)*r_left
        delta_y = math.cos(theta)*r_left

        return (delta_x, delta_y)