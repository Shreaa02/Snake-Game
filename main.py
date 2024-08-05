import time
import turtle
from turtle import Screen
from food import Food
from snake import Snake
from score import Score

s = Screen()
s.setup(width=600, height=500)
s.bgcolor("black")
s.title("Snake Game")
# for turning off animation
s.tracer(0)
sn = Snake()
m = sn.head
fd = Food()
sc = Score()
sn.create_snake()
game_is_on = True
while game_is_on:
    # for updating screen after every iteration
    s.update()
    # for causing delay so that the blocks show up as a single entity
    time.sleep(0.1)
    sn.move()
    s.listen()
    s.onkey(key="Left", fun=sn.move_lt)
    s.onkey(key="Right", fun=sn.move_rt)
    s.onkey(key="Up", fun=sn.move_up)
    s.onkey(key="Down", fun=sn.move_down)
    s.onkey(key="c", fun=sn.clear_scan)

    if m.distance(fd) < 14:
        turtle.clear()
        fd.change_pos()
        sc.score_board()
        sn.increase_snake()

    if m.xcor() < -280 or m.xcor() > 280 or m.ycor() < -250 or m.ycor() > 250:
        sc.end_game()
        game_is_on = False

    for body in sn.snake[1:]:
        if m.distance(body) < 5:
            game_is_on = False
            sc.end_game()



s.exitonclick()
