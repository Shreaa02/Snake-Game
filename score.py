from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setposition(0, 220)
        self.write(f" score : {self.score}", move=False, align='center', font=('Courier', 20, 'normal'))

    def score_board(self):
        self.score += 1
        self.clear()
        self.write(f" score : {self.score}", move=False, align='center', font=('Courier', 20, 'normal'))

    def end_game(self):
        self.clear()
        self.setposition(0, 0)
        self.write("Game over", move=False, align='center', font=('Courier', 20, 'normal'))

