'''
@Author: your name
@Date: 2020-01-18 15:01:24
@LastEditTime : 2020-01-18 19:50:58
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\编程测试\文件测试.py
'''
#注意，复制相对文件路径，这个有点抽风,而且这个貌似只能读取一遍
with open('vscode_python_test\编程测试\文件测试.txt') as file_object:
   
   #for line in file_object:
   # print(line)
   #逐行读取
   for line in file_object:
    print(line.rstrip())
   #content = file_object.read()
   #print(content)
#rstrip方法：删除 string 字符串末尾的指定字符（默认为空格）.
str = "     this is string example....wow!!!     ";
print (str.rstrip());
str = "88888888this is string example....wow!!!8888888";
print (str.rstrip('8'));

filename='文件测试.txt'
with open('vscode_python_test\编程测试\文件测试.txt') as ob:
   lines=ob.readlines()
#这个for语句中的lin的名字是可以随意定义的，但是这个lines必须是已经定义过的列表这些
for lin in lines:
   print(lin.rstrip())
#下面所利用的strip删除掉位于每行左边的空格
pi=''
for lin in lines:
   pi+=lin.strip()
print(pi)
print(len(pi))
'''
birthday=input("choose a number:")
if birthday in pi:
   print("yes")
else:
   print("no")
   '''