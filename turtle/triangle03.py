import turtle

screen = turtle.Screen()
screen.setup(400, 400)

t = turtle.Turtle()

def triangle(t, x, y, length):
    # TODO:請參考 square03.py 實作畫三角形的程式
    pass

triangle(t, 50, 50, 100)
triangle(t, -50, -50, 50)
triangle(t, -50, 50, 30)

screen.exitonclick()