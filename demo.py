from turtle import Turtle,Screen
screen = Screen()
screen.setup(width = 800, height=800)
tim = Turtle()
tim.penup()
tim.goto(-350,-350)
tim.pendown()
tim.circle(50)
screen.exitonclick()