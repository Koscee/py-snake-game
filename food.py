from random import randint
from turtle import Turtle

EDGE_BOUNDARY = 260


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("cyan")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = randint(-EDGE_BOUNDARY, EDGE_BOUNDARY)
        random_y = randint(-EDGE_BOUNDARY, EDGE_BOUNDARY)
        self.goto(random_x, random_y)
