'''
@Author: your name
@Date: 2020-02-15 20:19:00
@LastEditTime: 2020-03-02 20:17:04
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\基本语法\format运用.py
'''
#https://blog.csdn.net/qq_31821675/article/details/78751365
a = [1,2,3]
i = 1
#大括号紧跟format
b = a[int('{}'.format(i))]
print(b)
print(type('{}'.format(i)))

