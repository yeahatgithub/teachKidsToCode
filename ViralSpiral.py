# @Time    : 2018/4/23 14:32
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
import turtle
t = turtle.Pen()
t.penup()
turtle.bgcolor("black")

sides = int(turtle.numinput("边数", "小螺旋体有几条边？（2-6）", 4, 2, 6))
colors = ['red', 'yellow', 'blue', 'green', 'purple', 'orange']

#外循环
for m in range(100):
    t.forward(m * 4)
    position = t.position()
    heading = t.heading()
    print(position, heading)
    #内循环，绘制单个小螺旋体
    for n in range(int(m / 2)):
        t.pendown()
        t.pencolor(colors[n % sides])
        t.forward(2 * n)
        t.right(360 / sides - 2)
        t.penup()
    t.setx(position[0])
    t.sety(position[1])
    t.setheading(heading)
    t.left(360 / sides + 2)