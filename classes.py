from ev3dev2.motor import Motor, OUTPUT_A, OUTPUT_B
import math

class Bot:

    def __init__(self, name: str, leader: bool):
        
        self.name = name
        self.leader = bool

        self.motor_1 = Motor(OUTPUT_A)
        self.motor_2 = Motor(OUTPUT_B)

    def test(self):

        if self.leader:

            print(f"Hello, my name is {self.name} and I am the leader.")

        else:

            print(f"Hello, my name is {self.name} and I am not the leader.")

    def move_distance(self, delta_x : float, delta_y : float, speed: float):

        theta = math.atan(delta_y/delta_x)

        delta_p = math.sqrt(delta_x**2 + delta_y**2)

        self.move_theta(self, delta_p, theta, speed)

    def move_theta(self, delta_p : float, theta : float, speed : float):

        pass