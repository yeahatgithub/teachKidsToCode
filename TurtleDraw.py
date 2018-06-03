# @Time    : 2018/4/28 15:38
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
import turtle
t = turtle.Pen()
turtle.bgcolor("white")
t.pencolor('green')
t.width(99)
t.speed(0)
turtle.onscreenclick(t.setpos)
turtle.done()   #没有这一行，就会闪退