# @Time    : 2018/4/30 14:58
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT

import turtle
import random

t = turtle.Pen()
t.speed(0)
t.penup()
turtle.bgcolor("black")
t.pencolor('green')
t.width(2)

def new_spiral(x, y):
    m = random.randrange(8, 40)
    sides = random.randrange(3, 8)
    t.setposition(x, y)
    colors = ['red', 'yellow', 'blue', 'green', 'purple', 'orange']
    for n in range(m):
        t.pendown()
        t.pencolor(colors[n % min(sides, len(colors))])
        t.forward(2 * n)
        t.right(360 / sides - 2)
        t.penup()

turtle.onscreenclick(new_spiral)
turtle.done()