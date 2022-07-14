from turtle import Turtle

NUM_RANGE = 10
DISTANCE = 35

class Gameline(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.goto(0,300)
        self.pendown()
        self.setheading(270)
        for _ in range(NUM_RANGE):
            self.forward(DISTANCE)
            self.penup() 
            self.forward(DISTANCE)
            self.pendown() 