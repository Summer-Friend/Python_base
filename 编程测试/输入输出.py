'''
@Author: your name
@Date: 2020-01-18 14:50:01
@LastEditTime : 2020-01-18 15:00:44
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\编程测试\输入输出.py
'''
'''
hello = 'hello, runoob\n'
a=str(hello)
b=repr(hello)
print(hello)
print(a)
print(b)
for x in range(1, 11):
    #rjust貌似就是表示空格的意思
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # 注意前一行 'end' 的使用，因为Python的print第二次使用则代表换行
    print(repr(x*x*x).rjust(4))
    '''
x=2
print(str(x*x).rjust(2),str(x*x).rjust(12),end='      ')
print('hello')
print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # 注意前一行 'end' 的使用
print(repr(x*x*x).rjust(4))
print('hello')