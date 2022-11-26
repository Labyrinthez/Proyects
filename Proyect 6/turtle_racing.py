import turtle
from turtle import Turtle, Screen
from random import randint as r

my_screen = Screen()
turtle1 = Turtle()
turtle2 = Turtle()
turtle3 = Turtle()
turtle4 = Turtle()
turtle5 = Turtle()
turtle6 = Turtle()

turtle1.color("black")
turtle2.color("coral")
turtle3.color("green")
turtle4.color("blue")
turtle5.color("red")
turtle6.color("purple")

turtle1.shape("turtle")
turtle2.shape("turtle")
turtle3.shape("turtle")
turtle4.shape("turtle")
turtle5.shape("turtle")
turtle6.shape("turtle")

turtle1.penup()
turtle2.penup()
turtle3.penup()
turtle4.penup()
turtle5.penup()
turtle6.penup()

my_screen.setup(width=500, height=400)

turtle1.goto(x=-230, y=0)
turtle2.goto(x=-230, y=30)
turtle3.goto(x=-230, y=60)
turtle4.goto(x=-230, y=-30)
turtle5.goto(x=-230, y=-60)
turtle6.goto(x=-230, y=-90)

user_bet = my_screen.textinput(title="Make your bet", prompt="Select: black, coral, green, blue, red or purple? ")
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
counter6 = 0
while True:
    a = r(1, 20)
    b = r(1, 20)
    c = r(1, 20)
    d = r(1, 20)
    e = r(1, 20)
    f = r(1, 20)
    turtle1.forward(a)
    turtle2.forward(b)
    turtle3.forward(c)
    turtle4.forward(d)
    turtle5.forward(e)
    turtle6.forward(f)
    counter1 += a
    counter2 += b
    counter3 += c
    counter4 += d
    counter5 += e
    counter6 += f
    if counter1 > 500 or counter2 > 500 or counter3 > 500 or counter4 > 500 or counter5 > 500 or counter6 > 500:
        break
my_screen.exitonclick()
