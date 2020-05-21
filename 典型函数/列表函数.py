'''
@Author: your name
@Date: 2020-02-16 14:58:33
@LastEditTime: 2020-02-23 14:11:42
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\基本语法\列表函数.py
'''
#下面这两个方法对于元组，字典也适用
#1.cmp() 方法用于比较两个列表的元素。不过这个貌似3.x版本没了。。。
list1, list2 = [123, 'xyz'], [456, 'abc']
"""
print (cmp(list1, list2))
print (cmp(list2, list1))
list3 = list2 + [786]
print (cmp(list2, list3))
"""

#2.len() 方法返回列表元素个数。


#max,min函数

#元组转列表
aTuple = (123, 'xyz', 'zara', 'abc');
aList = list(aTuple)
print ("列表元素 : ", aList)

#3.set，将 [ ] 变成了 { }并且它去掉了list中的重复元素。。。还可以进行与或运算
a = [1,1,2,3,4]
b = [0,1,2,3,6]
print(list(set(a) & set(b)))

#关于索引
a=['a',2,3]
#enumerate会将数组或列表组成一个索引序列
for i,j in enumerate(a):
    print(i,'',j)
