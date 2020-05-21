'''
@Author: your name
@Date: 2020-03-10 17:23:24
@LastEditTime: 2020-03-11 13:58:39
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\数据可视化\turtle库\彩虹.py
'''
import turtle                                                          #引用turtle库
q = turtle.Pen()                                                       #构造画笔
turtle.bgcolor("black")                                                #画布的背景颜色为黑色
sides = 7                                                              #定义变量控制环绕程度
colors = ["red","orange","yellow","green","cyan","blue","purple"]
for x in range(360):                                                   #for循环控制画笔的走向与速度
    q.speed(35)
    q.pencolor(colors[x%sides])
    q.forward(x*3/sides+x)
    q.left(360/sides+1)
    q.width(x*sides/200)
