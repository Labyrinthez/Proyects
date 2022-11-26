from turtle import Turtle
from random import uniform, randint


class Car(Turtle):
    def __init__(self):
        super(Car, self).__init__()
        self.penup()
        self.color((uniform(0, 1), uniform(0, 1), uniform(0, 1)))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.car_speed = 20
        self.setheading(180)
        self.cars = []
        self.goto_random()
        self.time_speed = .2

    def move(self):
        self.forward(self.car_speed)
        for i in range(0, len(self.cars) - 1):
            self.cars[i].forward(self.car_speed)

    def generate_random_cars(self):
        for i in range(0, 30):
            new_car = Car()
            self.cars.append(new_car)
        new_car.goto(1000, 1000)

    def goto_random(self):
        y = randint(-250, 250)
        x = randint(-250, 250)
        self.goto(x, y)

    def collision(self, player):
        for i in range(0, len(self.cars) - 1):
            distance_x = abs(player.xcor() - self.cars[i].xcor())
            distance_y = abs(player.ycor() - self.cars[i].ycor())
            if distance_x < 30 and distance_y < 20:
                return True

    def restart_cars(self):
        for i in range(0, len(self.cars) - 1):
            self.cars[i].goto_random()

    def change_position(self):
        if self.xcor() < -280:
            self.goto(300, self.ycor())
        for i in range(0, len(self.cars) - 1):
            if self.cars[i].xcor() < -280:
                self.cars[i].goto(280, self.cars[i].ycor())
