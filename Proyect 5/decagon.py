from turtle import Turtle, Screen

timmy = Turtle()
my_screen = Screen()
timmy.shape("turtle")
timmy.color("lime")


def triangle():
    for i in range(0, 3):
        timmy.forward(100)
        timmy.right(120)


def square():
    for i in range(0, 4):
        timmy.forward(100)
        timmy.right(90)


def pentagon():
    for i in range(0, 5):
        timmy.forward(100)
        timmy.right(360/5)


def hexagon():
    for i in range(0, 6):
        timmy.forward(100)
        timmy.right(360/6)


def heptagon():
    for i in range(0, 7):
        timmy.forward(100)
        timmy.right(360/7)


def octagon():
    for i in range(0, 8):
        timmy.forward(100)
        timmy.right(360/8)


def nonagon():
    for i in range(0, 9):
        timmy.forward(100)
        timmy.right(360/9)


def decagon():
    for i in range(0, 10):
        timmy.forward(100)
        timmy.right(360/10)


triangle()
square()
pentagon()
hexagon()
heptagon()
octagon()
nonagon()
decagon()
my_screen.exitonclick()