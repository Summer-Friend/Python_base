'''
@Author: your name
@Date: 2020-02-16 18:21:13
@LastEditTime: 2020-02-16 18:21:13
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\基本语法\元组函数.py
'''
#tuple() 函数不是改变值的类型，而是返回改变类型后的值，原值不会被改变：

test_list1 = ('a','b','c')
test_list2 = ['x','y','z']
test_tuple = tuple(test_list2)
# test_list2 可以修改，tuple() 函数不是改变值的类型，而是返回改变类型后的值，原值不会被改变
test_list2[2] = '这是修改的'
#下面这行报错，元组不可修改
# test_list1[2]='这是修改的'
print(test_list1)
print(test_list2)
print(test_tuple)
