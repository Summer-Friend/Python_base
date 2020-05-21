'''
@Author: your name
@Date: 2020-01-16 19:54:01
@LastEditTime : 2020-01-16 20:16:07
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\编程测试\语句测试.py
'''
n=10
sum=0
count=1
#python中的控制语句不用大括号，用冒号控制
while count<=n:
 sum=sum+count
 count+=1
 print("count小于：",n)
else:
    print("count大于或等于:",n)
print("sum:",sum)
for i in range(0,10,2):
 print(i)
