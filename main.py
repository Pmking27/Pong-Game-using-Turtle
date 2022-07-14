from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
from game_line import Gameline
import time

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()
line=Gameline()

screen.listen() 
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down,"s") 

game_should_on=True

while game_should_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() >280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle)<50 and ball.xcor() >330:
        ball.bounce_x() 
    if ball.distance(l_paddle)<50 and ball.xcor() <-330:
        ball.bounce_x()

    if ball.xcor() > 410:
        ball.reset_position()
        scoreboard.l_point()
        
    if ball.xcor() < -410:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()