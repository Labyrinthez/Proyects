from turtle import Turtle, Screen

timmy = Turtle()
my_screen = Screen()
timmy.shape("turtle")
timmy.color("lime")
for a in range(0, 4):
    for i in range(0, 10):
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()
        timmy.forward(10)
    timmy.right(90)
my_screen.exitonclick()