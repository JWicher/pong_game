from turtle import Turtle

class Middle_line(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed('fastest')
        self.pencolor('white')
        self.pensize(5)
        self.penup()
        self.goto(0, 300)
        self.setheading(270)
        self.draw_line()

    def draw_line(self):

        while self.ycor() > -300:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
