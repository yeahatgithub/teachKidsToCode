# @Time    : 2018/4/28 15:48
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
import turtle
pen = turtle.Pen()
pen.speed(0)
pen.turtlesize(2, 2, 2)


def up():
    pen.forward(30)

def left():
    pen.left(60)

def right():
    pen.right(60)

turtle.onkeypress(up, 'Up')
turtle.onkeypress(left, 'Left')
turtle.onkeypress(right, 'Right')
turtle.listen()
turtle.done()