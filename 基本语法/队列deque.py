'''
@Author: your name
@Date: 2020-02-22 16:06:10
@LastEditTime: 2020-02-22 16:17:48
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\基本语法\collections deque.py
'''
from collections import deque
d = deque('hello')
for elem in d:
    print(elem.upper())

d.append('j')  #默认在最后面添加
d.appendleft('N')  #在前面添加
d.pop() #默认去除最后一个
d.popleft() #默认去除第一个
d.extend('abc')  #一次添加多个元素

'''
a = 'abc'
for element in a:
    print(element.upper())

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry 入队
queue.append("Graham")          # Graham 入队
queue.popleft()                 # 队首元素出队
#输出: 'Eric'
queue.popleft()                 # 队首元素出队
#输出: 'John'
print(queue)                           # 队列中剩下的元素
#输出: deque(['Michael', 'Terry', 'Graham'])

'''


