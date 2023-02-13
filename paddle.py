import random
from turtle import Turtle

direction = {
    "UP": 90,
    "DOWN": 270
}

starting_positions = {
    "user": (-450, 0),
    "comp": (450, 0),
}

move_limit = {
    "upper": 240,
    "lower": -240,
}

move_step = 30

class Paddle(Turtle):
    def __init__(self, paddle_type):
        super().__init__()
        self.paddle_segments_positions = []
        self.set_position_on_the_board(paddle_type)

        self.shape('square')
        self.shapesize(stretch_len=5)
        self.color('white')
        self.speed('fastest')
        self.penup()
        self.setheading(random.choice([90, 270]))

    def set_position_on_the_board(self, paddle_type):
        self.goto(starting_positions[paddle_type])

    def move_automatically(self):
        if self.ycor() >= move_limit["upper"]:
            self.setheading(direction["DOWN"])

        elif self.ycor() <= move_limit["lower"]:
            self.setheading(direction["UP"])

        self.forward(move_step)


    def move_down(self):
        if self.ycor() <= move_limit["lower"]:
            return

        self.setheading(direction["DOWN"])
        self.forward(move_step)

    def move_up(self):
        if self.ycor() >= move_limit["upper"]:
            return

        self.setheading(direction["UP"])
        self.forward(move_step)
