'''
@Author: your name
@Date: 2020-01-14 21:26:20
@LastEditTime : 2020-02-13 18:57:22
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\菜鸟教程\列表.py
'''
#字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
list=[1,2,3,4,5]
for i in list:
    list_num=list[0]
    list_author=list[1]
    list_a=list[1]
    list_4=list[3]
print(list_num,list_author)
'''
#修改键值
dict['Name']=7
print("修改后的dict['Name']",dict['Name'])
#不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
#这一步操作是打印所有字典的头
for item in dict:
    print(item)
dict1=[1, 2, 3, 4, 5]
dict2=['a','b','c','d','e']
dict3=[4, 5, 6, 7, 8]
print([3*x for x in dict1])
print([4*x for x in dict1 if x>3])
print(dict2)
#print([x+y for x in dict1 for y in dict2])
print([x+y for x in dict1 for y in dict3])
print([dict1[i]+dict3[i] for i in range (len(dict1))])
#roung代表四舍五入，后面那位是指小数位数
print([str(round(355/113,i)) for i in range(1,6)])
'''

dict = {'Name': 'Zara', 'Age': 27}
#get用来获取键值
print "Value : %s" %  dict.get('Age')
