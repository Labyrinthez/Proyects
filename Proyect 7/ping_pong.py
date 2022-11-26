from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_bar import Scoreboard
import time


game_is_on = True
screen = Screen()
screen.tracer(0)
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.title("Ping - Pong")
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
while game_is_on:
    time.sleep(.1)
    screen.update()
    ball.move_ball()
    screen.listen()
    screen.onkey(fun=r_paddle.paddle_up, key="Up")
    screen.onkey(fun=r_paddle.paddle_down, key="Down")
    screen.onkey(fun=l_paddle.paddle_up, key="w")
    screen.onkey(fun=l_paddle.paddle_down, key="s")
    # Detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if abs(ball.xcor() - r_paddle.xcor()) < 30 and abs(ball.ycor() - r_paddle.ycor()) < 60:
        ball.x_move += 5
        ball.bounce_x()
    if abs(ball.xcor() - l_paddle.xcor()) < 30 and abs(ball.ycor() - l_paddle.ycor()) < 60:
        ball.x_move -= 5
        ball.bounce_x()
    # Out of bounce
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
