'''
@Author: your name
@Date: 2020-02-16 18:21:01
@LastEditTime: 2020-03-05 12:09:20
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\基本语法\字典函数.py
'''
#字典更新
dict1 = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex': 'female' }
dict1.update(dict2)
print(dict1)

dict = {'Name': 'Zara', 'Age': 7};
print(dict)
#返回字符串类型
print ("Equivalent String : %s" % str (dict))
#返回键，值
print(dict.keys(),' ',dict.values())

# items() 函数以列表返回可遍历的(键, 值) 元组数组。
dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
print ("字典值 : %s" %  dict.items())
# 遍历字典列表
for key,values in  dict.items():
    print (key,values)
    
    
#运用
a = {'a':[{'b':1},{'c':2},{'d':3}]}
b = {}
b['1'] = a['a'][0]
b['2'] = a['a'][1]
b['3'] = a['a'][2]
print(len(a))
print(b)

a = {'a':[{'b':[1,2],'c':[2,3]}, {'b':[3,4],'c':[4,5]}]}
print(a['a'][0]['b'])
print(len(a['a']))