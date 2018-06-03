# @Time    : 2018/4/27 15:30
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT

import random
import turtle

colors = ['red', 'yellow', 'blue', 'green', 'purple', 'orange']
t = turtle.Pen()
t.penup()
turtle.bgcolor("black")
for i in range(100):
    size = random.randrange(10, 30)
    x = random.randrange(-turtle.window_width() // 2, turtle.window_width() // 2)
    y = random.randrange(-turtle.window_width() // 2, turtle.window_width() // 2)
    color = random.choice(colors)
    t.pencolor(color)
    t.setposition(x, y)
    t.pendown()
    for m in range(size):
        t.forward(2 * m)
        t.right(91)
    t.penup()
