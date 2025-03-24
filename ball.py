from turtle import Turtle
from random import choice

UP_RIGHT = 45
UP_LEFT = 135
DOWN_RIGHT = 315
DOWN_LEFT = 225

DIRECTIONS = [UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT]

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.speed('normal')
        self.trajectory = choice(DIRECTIONS)

    # def hit_wall(self):
    #     if self.trajectory in (UP_RIGHT, DOWN_LEFT):
    #         self.trajectory += 90
    #     elif self.trajectory in (DOWN_RIGHT, UP_LEFT):
    #         self.trajectory -= 90

    # def hit_ceiling_floor(self):
    #     if self.trajectory == UP_RIGHT:
    #         self.trajectory = DOWN_RIGHT
    #     elif self.trajectory == UP_LEFT:
    #         self.trajectory = DOWN_LEFT
    #     elif self.trajectory == DOWN_RIGHT:
    #         self.trajectory = UP_RIGHT
    #     elif self.trajectory == DOWN_LEFT:
    #         self.trajectory = UP_LEFT

    def hit(self):
        self.trajectory = (self.trajectory + 180) % 360

def hit_test(angle):
    angle = (angle + 180) % 360
    return angle


for direction in DIRECTIONS:
    print(hit_test(direction))

# traj = choice(DIRECTIONS)

# print(traj)