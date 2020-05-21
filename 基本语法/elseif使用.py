'''
@Author: your name
@Date: 2020-01-13 20:58:19
@LastEditTime : 2020-01-14 20:01:18
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\菜鸟教程.py
'''
'''
a = 21
b = 10
c = 0
 
if ( a == b ):
   print ("1 - a 等于 b")
else:
   print ("1 - a 不等于 b")
 
if ( a != b ):
   print ("2 - a 不等于 b")
else:
   print ("2 - a 等于 b")
 
if ( a < b ):
   print ("3 - a 小于 b")
else:
   print ("3 - a 大于等于 b")
 
if ( a > b ):
   print ("4 - a 大于 b")
else:
   print ("4 - a 小于等于 b")
 
# 修改变量 a 和 b 的值
a = 5
b = 20
if ( a <= b ):
   print ("5 - a 小于等于 b")
else:
   print ("5 - a 大于  b")
 
if ( b >= a ):
   print ("6 - b 大于等于 a")
else:
   print ("6 - b 小于 a")
'''
#Python语言对于elseif使用较为严格，对于缩进也有一定的控制
a=12
b=11
if a==b:             #此处的if和else语句全都要在同一列上
    print ("等于")
elif a<b:
     print("小于")
else:
      print("大于")  #即此处上下两条语句必须在同一缩进上才行，不然报错
      print("你好")
    