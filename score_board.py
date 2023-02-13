from turtle import Turtle

FONT = ('Courier', 50, 'normal')
ALIGN = 'center'

class Score_board(Turtle):

    def __init__(self):
        super().__init__()

        self.score_user = 0
        self.score_comp = 0

        self.hideturtle()
        self.goto(0, 250)
        self.color('white')
        self.draw_score_board()

    def draw_score_board(self):
        self.clear()
        self.write(f"{self.score_user} {self.score_comp}", align=ALIGN, font=FONT)

    def user_scores(self):
        self.score_user += 1
        self.draw_score_board()

    def comp_scores(self):
        self.score_comp += 1
        self.draw_score_board()
