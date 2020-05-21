'''
@Author: your name
@Date: 2020-03-10 17:27:29
@LastEditTime: 2020-03-10 17:49:32
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\典型函数\随机random.py
'''
import random 
'''
#random.randint(a,b)用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b。
print(random.randint(0,2))

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(3):
    slice = random.sample(list, 5)  # 从list中随机获取5个元素，作为一个片断返回
    print(slice)
    print(list, '\n')  # 原有序列并没有改变
'''
#生成一个[m,n)之间以k为步长的随机整数
for i in range(5):
    print(random.randrange(0,100,5))
    
print(random.random())#函数是这个模块中最常用的方法了，它会生成一个随机的浮点数，范围是在0.0~1.0之间。

print(random.uniform(0.1,2))#正好弥补了上面函数的不足，它可以设定浮点数的范围，一个是上限，一个是下限。

#可以从任何序列，比如list列表中，选取一个随机的元素返回，可以用于字符串、列表、元组等。
foo = ['a', 'b', 'c', 'd', 'e']
print (random.choice(foo))

#如果你想将一个序列中的元素，随机打乱的话可以用这个函数方法
#在Python2中，range函数输出的是list类型，而Python3中输出的是range类型。
li=list(range(20))
random.shuffle(li)
print (li)
