from turtle import Turtle

class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
    def create_snake(self):
        for i in range(0, 3):
            t = Turtle(shape="square")
            t.speed("slowest")
            t.color("white")
            t.penup()
            t.heading()
            t.setposition(x=i * (-20), y=0)
            self.snake.append(t)

    def move(self):
        for sq in range(len(self.snake) - 1, 0, -1):
            nx = self.snake[sq - 1].xcor()
            ny = self.snake[sq - 1].ycor()
            self.snake[sq].goto(nx, ny)
        self.head.fd(20)

    def move_lt(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def move_rt(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def clear_scan(self):
        self.head.clear()

    def increase_snake(self):
        t = Turtle(shape="square")
        t.speed("slowest")
        t.color("white")
        t.penup()
        t.heading()
        self.snake.append(t)


