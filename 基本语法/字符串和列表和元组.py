'''
@Author: your name
@Date: 2020-01-14 19:58:51
@LastEditTime: 2020-03-05 11:04:48
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\字符串.py
'''
'''
字符串是 Python 中最常用的数据类型。我们可以使用引号( ' 或 " )来创建字符串。
创建字符串很简单，只要为变量分配一个值即可
访问字符串中的值
不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。
其中也涉及到了列表的使用，类似于数组，列表也支持拼接，嵌套（这个类似于二维的操作）
'''
var1='hello world'
print("var1[0]:",var1[0])
print("var1[1:4]:",var1[1:4])    #可以使用方括号来截取字符串
if("h" in var1):
   print("h在var1中")
if( "H" in var1) :
    print("H 在变量 a 中")
else :
    print("H 不在变量 a 中")

var2 = 'Hello World!'
print ("已更新字符串 : ", var2[:6] + 'Runoob!')


#列表#####################################################
#删除功能del的使用
list = ['Google', 'Runoob', 1997, 2000] 
#和c++类似，她也是从0开始，但是结束是到n-1结束
print("利用列表进行输出：",list[0:2])
#从开始到最后一个元素
print(list[0:])
print ("原始列表 : ", list)
del list[2]
print("更新后的列表",list)
#append在列表末尾添加新的对象
list1 = ['Google', 'Runoob', 'o','Taobao']
list1.append('Baidu')
print ("更新后的列表 : ", list1)
#标点符号英文输入
print ("列表中O出现次数：",list1.count('o'))
print ("Runoob 元素个数 : ", list1.count('Runoob'))
#列表的添加元素
c = [1,2,3]
c.append(4)
#print(c+4)   #直接加数字是错误的
print(c+[4])
#关于列表的输出，元组也是类似的
a=[1,2,3,4,5,6]
print(a[5:1:-1])  #从第五位到第三位倒序输出，-1位步长
print(a[::-1])   #倒序输出
print(a[::-2])   #隔一位倒序输出
#
a=[(1,2)]
print(a[0])



#元组###################################
list2 = ('Google', 'Runoob', 1997, 2000)
#和c++类似，她也是从0开始，但是结束是到n-1结束
print("利用元组进行输出：",list2[0:2])
#元组不支持修改，会报错：TypeError: 'tuple' object does not support item assignment
a = (1,2,3)
a[1] = 4