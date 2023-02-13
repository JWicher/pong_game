from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.move_speed = 0.1
        self.move_y = -10
        self.move_x = -10

    def move(self):
        new_x_cor = self.xcor() + self.move_x
        new_y_cor = self.ycor() + self.move_y
        self.goto(new_x_cor, new_y_cor)

    def bounce(self):
        self.move_y *= -1

    def hit_by_paddle(self):
        self.move_x *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.home()
        self.move_x *= -1
        self.move_speed = 0.1
