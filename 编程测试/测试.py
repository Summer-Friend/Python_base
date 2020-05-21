'''
@Author: your name
@Date: 2020-01-18 21:56:15
@LastEditTime : 2020-01-19 10:22:04
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\编程测试\测试.py
'''
'''
try:
 #'a'表示附加到源文件上
 with open('测试1.txt','a') as change:
    content=change.read()
except SyntaxError:
 print("This is SyntaxError")
'''
filename='alice.txt'
with open('测试1.txt') as change:
    content=change.read()
with open('测试1.txt','w') as change:
    change.write("fuck")
print(content)
