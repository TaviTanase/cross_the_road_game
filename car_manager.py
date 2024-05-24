from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self, y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.goto(280, y)
        self.color(random.choice(COLORS))


class Car_manager():
    def __init__(self):
        self.cars = []
        self.icars=0
        self.speed = 5

    def create_cars(self):
        temp=0
        y = random.randint(-40, 45)

        if y > -27 and y % 2 != 0  and y < 29 and self.icars<30:
            newcar = Car(y*10)
            self.cars.append(newcar)
            self.icars +=1

    def move(self):
        for car in self.cars[:]:
            car.forward(self.speed)
            if car.xcor() < -310:
                car.goto(280,random.randint(-26, 28)*10)

    def update(self):
        self.speed=self.speed+5

