from turtle import Turtle, Screen
from car import Car
import time
GAME_IS_ON = True
god_mode_on = False


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-175, 0)
        self.write("GAME OVER", font=("courier", 50, "normal"))


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.print_level()

    def increase_level(self):
        self.level += 1
        self.print_level()

    def print_level(self):
        self.clear()
        self.goto(-280, 270)
        self.write("Level: {}".format(self.level), font=("courier", 15, "normal"))


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.turtle_speed = 20

    def go_up(self):
        self.forward(self.turtle_speed)

    def go_down(self):
        self.forward(self.turtle_speed * -1)

    def reset_position(self):
        self.goto(0, -280)


def commands():
    global god_mode_on
    if screen.textinput(title="Cheats", prompt="Write the command below: ") == "god mode":
        god_mode_on = True
        cheat = Player()
        cheat.hideturtle()
        cheat.goto(100, 270)
        cheat.write("Cheats active!", font=("courier", 15, "normal"))
    else:
        god_mode_on = False


screen = Screen()
screen.title("Turtle crossing road game")
screen.setup(width=600, height=600)
screen.tracer(0)

level = Level()

player = Player()
player.setheading(90)

car = Car()
car.generate_random_cars()

while GAME_IS_ON:
    if player.ycor() > 250:
        player.reset_position()
        level.increase_level()
        car.restart_cars()
        car.time_speed *= .9
    screen.update()
    screen.listen()
    screen.onkey(fun=commands, key="t")
    screen.onkey(fun=player.go_up, key="w")
    screen.onkey(fun=player.go_down, key="s")
    time.sleep(car.time_speed)
    car.move()
    if not god_mode_on:
        if car.collision(player):
            break
    car.change_position()
game_over = GameOver()
screen.update()
screen.exitonclick()
