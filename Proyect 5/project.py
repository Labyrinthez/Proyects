import turtle
from turtle import Turtle, Screen
import random
import colorgram

color = colorgram.extract("image.jpg", 10)
colors = []
turtle.colormode(255)
for i in range(0, 10):
    r = color[i].rgb[0]
    g = color[i].rgb[1]
    b = color[i].rgb[2]
    colors.append((r, g, b))
timmy = Turtle()
my_screen = Screen()
timmy.shape("turtle")
timmy.color("lime")
timmy.speed("slow")
timmy.hideturtle()
timmy.speed(0)
timmy.pensize(10)
row = 20
# timmy.setheading(225)
# timmy.forward(300)
# timmy.setheading(0)
for b in range(0, 10):
    for a in range(0, 10):
        timmy.pencolor(colors[random.randint(0, len(colors) - 1)])
        timmy.pendown()
        timmy.forward(1)
        timmy.penup()
        timmy.forward(20)
    timmy.penup()
    timmy.goto(0, row)
    row += 20
my_screen.exitonclick()
