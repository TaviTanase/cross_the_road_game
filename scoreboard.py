from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(x=-250, y=260)
        self.hideturtle()
        self.color("black")
        self.write(f"level {self.level}", move=False, align="center", font=("Arial", 13, "normal"))

    def update(self):
        self.level+=1
        self.clear()
        self.write(f"level {self.level}", move=False, align="center", font=("Arial", 13, "normal"))

    def gameover(self):
        self.color("white")
        self.clear()
        self.goto(0, 0)
        self.color("black")
        self.write("GAME OVER", move=False, align="center", font=("Arial", 25, "normal"))
