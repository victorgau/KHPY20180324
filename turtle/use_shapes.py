# 測試一下 shapes 模組中的程式

import turtle
from shapes import square, triangle

screen = turtle.Screen()
screen.setup(400, 400)

t = turtle.Turtle()

triangle(t, 50, 50, 100)
triangle(t, -50, -50, 50)
triangle(t, -50, 50, 30)

screen.exitonclick()