from turtle import Turtle
MOVE_DISTANCE = 20

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.reset()
        self.setheading(90)

    def move(self):
        self.goto(self.xcor(),self.ycor()+MOVE_DISTANCE)

    def reset(self):
        self.goto(x=0,y=-280)