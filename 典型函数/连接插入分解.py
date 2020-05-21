'''
@Author: your name
@Date: 2020-02-16 14:51:39
@LastEditTime: 2020-02-23 13:25:18
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\基本语法\连接符号.py
'''
#join
str = "-";
seq = ("a", "b", "c"); # 字符串序列
print (str.join( seq ))

#split
str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print (str.split( ))      # 以空格为分隔符，包含 \n
print (str.split(' ', 1 )) # 以空格为分隔符，分隔成两个

#list.insert(index, obj):index -- 对象 obj 需要插入的索引位置。obj -- 要插入列表中的对象。
aList = [123, 'xyz', 'zara', 'abc']
aList.insert( 3, 2009)
print ("Final List : ", aList)

#pop
list1 = ['Google', 'Runoob', 'Taobao']
list_pop=list1.pop(1)
print ("删除的项为 :", list_pop)
print ("列表现在为 : ", list1)

#remove
li = ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
li.remove("z")  
li.remove("new")    # 删除首次出现的一个值


#extend列表连接
aList = [123, 'xyz', 'zara', 'abc', 123];
bList = [2009, 'manni'];
aList.extend(bList)
print ("Extended List : ", aList)

#append
aList = [123, 'xyz', 'zara', 'abc'];
aList.append( 2009 );
print ("append List : ", aList)

#insert
aList = [123, 'xyz', 'zara', 'abc'];
aList.insert(2, 'new')
print(aList)

#strip:用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
#注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
str = "00000003210Runoob01230000000"; 
print (str.strip( '0' ))  # 去除首尾字符 0
 
str2 = "   Runoob      ";   # 去除首尾空格
print (str2.strip())

#rstrip:删除 string 字符串末尾的指定字符（默认为空格）.
str = "     this is string example....wow!!!     ";
print (str.rstrip())
str = "88888888this is string example....wow!!!8888888";
print (str.rstrip('8'))

