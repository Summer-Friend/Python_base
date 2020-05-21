'''
@Author: your name
@Date: 2020-01-19 16:11:05
@LastEditTime: 2020-02-23 16:39:32
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\基本语法\int_use.py
'''
a=1.2
print(a, end=' ')
print(a)

# 九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}'.format(j, i, i*j), end=' ')
    print()
    
#通过指定end参数的值，可以取消在末尾输出回车符，实现不换行