from turtle import Screen, Turtle
import random
rgb_colors = [(202, 164, 130),
              (228, 240, 245), (162, 167, 32),
              (236, 67, 126), (237, 78, 54), (150, 54, 101), (238, 219, 83)]

screen = Screen()
screen.setup(width=800, height=800)
screen.colormode(255)
tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.setpos((-350, -350))
tim.position()-
tim.penup()
tim.hideturtle()
for row in range(10):
    tim.setpos(-350, -350 + 50*row)
    for column in range(10):
        tim.dot(20, random.choice(rgb_colors))
        tim.setpos(tim.xcor()+50, tim.ycor())
screen.exitonclick()