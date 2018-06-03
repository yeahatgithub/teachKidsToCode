# @Time    : 2018/4/22 15:43
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT

import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ['red', 'yellow', 'blue', 'green']

name = turtle.textinput("输入名字", "你的名字：")
for x in range(100):
    t.pencolor(colors[x%4])
    t.penup()
    t.forward(x * 4)
    t.pendown()
    t.write(name, font = ('Arial', int( (x + 4) / 4), "bold"))
    t.left(92)