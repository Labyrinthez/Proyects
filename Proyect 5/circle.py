from turtle import Turtle, Screen
import random

timmy = Turtle()
my_screen = Screen()


def circle_mandala():
    timmy.shape("turtle")
    timmy.color("lime")
    counter = 0
    timmy.speed(0)
    timmy.hideturtle()
    while counter != 360:
        timmy.pencolor(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
        timmy.circle(50)
        timmy.right(5)
        timmy.circle(50)
        counter += 5


circle_mandala()
my_screen.exitonclick()
