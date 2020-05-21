'''
@Author: your name
@Date: 2020-03-11 15:37:21
@LastEditTime: 2020-03-11 15:41:45
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\数据可视化\turtle库\太阳花.py
'''
import turtle
import time
 
# 同时设置pencolor=color1, fillcolor=color2
turtle.color("red", "yellow")
 
turtle.begin_fill()
for _ in range(50):
    turtle.forward(200)
    turtle.left(170)
turtle.end_fill()

#turtle.mainloop()
