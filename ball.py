from turtle import Turtle

class Ball(Turtle):
    def __init__(self) :
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.new_xcor = 10
        self.new_ycor = 10
        self.move_speed = 0.1

    def move(self):
        new_x=self.xcor()+self.new_xcor
        new_y=self.ycor()+self.new_ycor
        self.goto(new_x,new_y) 

    def bounce_x(self):
        self.new_xcor *= -1
        self.move_speed *= 0.9

    def bounce_y(self):
        self.new_ycor *= -1

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()    
    
