from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.speed("fastest")
        self.clear()
        self.change_pos()

    def change_pos(self):
        # x = self.xcor()
        # y = self.ycor()
        new_x = randint(-280, 280)
        new_y = randint(-230, 230)
        self.setpos(new_x, new_y)
        # return self.setpos(new_x, new_y)
