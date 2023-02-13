from turtle import Screen
import time

from middle_line import Middle_line
from score_board import Score_board
from ball import Ball
from paddle import Paddle

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor('black')
screen.title("Pong game")
screen.tracer(0)
screen.listen()

middle_line = Middle_line()
score_board = Score_board()
ball = Ball()
paddle_user = Paddle("user")
paddle_comp = Paddle("comp")

game_is_on = True

screen.onkeypress(paddle_user.move_up, 'w')
screen.onkeypress(paddle_user.move_down, 's')

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    paddle_comp.move_automatically()

    if ball.ycor() <= -285 or ball.ycor() >= 285:
        ball.bounce()

    user_hit_a_ball = ball.distance(paddle_user) < 50 and ball.xcor() < -420
    comp_hit_a_ball = ball.distance(paddle_comp) <= 50 and ball.xcor() > 420

    if user_hit_a_ball or comp_hit_a_ball:
        ball.hit_by_paddle()

    if ball.xcor() > 500:
        score_board.user_scores()
        ball.reset_position()
        time.sleep(0.5)

    if ball.xcor() < -500:
        score_board.comp_scores()
        ball.reset_position()
        time.sleep(0.5)

    screen.update()

screen.exitonclick()
