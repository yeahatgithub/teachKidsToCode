# @Time    : 2018/4/21 12:13
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
import turtle
turtle.bgcolor('black')
t = turtle.Pen()
colors = ['red', 'yellow', 'blue', 'orange', 'green', 'purple']
sides = 6
for x in range(360):
    t.pencolor(colors[x % sides])
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + 1)
    t.width(x * sides / 200)
    t.left(90)