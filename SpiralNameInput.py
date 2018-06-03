# @Time    : 2018/4/22 15:43
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT

import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'white', 'brown']

name = turtle.textinput("输入名字", "你的名字：")
sides = int(turtle.numinput("边数输入", "有多少条边？(1-8):"))
for x in range(100):
    t.pencolor(colors[x%sides])
    t.penup()
    t.forward(x * sides // 3)
    t.pendown()
    t.write(name, font = ('Arial', int( (x + sides) / sides), "bold"))
    t.left(360 / sides + 2)