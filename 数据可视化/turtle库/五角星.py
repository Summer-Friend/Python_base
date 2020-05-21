'''
@Author: your name
@Date: 2020-03-11 15:42:45
@LastEditTime: 2020-03-11 15:46:47
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\数据可视化\turtle库\五角星.py
'''
import turtle
import time
 
turtle.pensize(5)
turtle.pencolor("yellow")
turtle.fillcolor("red")
 
turtle.begin_fill()
for _ in range(5):
  turtle.forward(200)
  turtle.right(144)
turtle.end_fill()
time.sleep(2)
 
#抬笔，可以防止弄脏画布
turtle.penup()
turtle.goto(-150,-120)
turtle.color("violet")
turtle.write("Done", font=('Arial', 40, 'normal'))
 
turtle.mainloop()

