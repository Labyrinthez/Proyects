from turtle import Turtle, Screen
import random

timmy = Turtle()
my_screen = Screen()

def random_walk(rounds):
    timmy.shape("turtle")
    timmy.color("lime")
    timmy.speed(0)
    timmy.pensize(10)
    directions = [90, 180, 270, 360]
    timmy.hideturtle()
    for i in range(0, rounds):
        timmy.pencolor(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
        angle = random.choice(directions)
        timmy.right(angle)
        timmy.forward(20)


random_walk(1000)
my_screen.exitonclick()
