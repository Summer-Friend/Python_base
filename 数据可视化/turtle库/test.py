'''
@Author: your name
@Date: 2020-03-10 17:25:06
@LastEditTime: 2020-03-10 17:25:34
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\数据可视化\turtle库\test.py
'''
sides = 7                                                              #定义变量控制环绕程度
colors = ["red","orange","yellow","green","cyan","blue","purple"]
for x in range(360):                                                   #for循环控制画笔的走向与速度
    print(colors[x%sides])