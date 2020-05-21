'''
@Author: your name
@Date: 2020-01-18 20:00:19
@LastEditTime : 2020-01-20 14:52:45
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\编程测试\错误异常.py
'''
class MyClass:
    """一个简单的类实例"""
    i = 12345
    #使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例
    def f(self):
        return 'hello world'
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.p = imagpart
# 实例化类
x = MyClass(3,4)
 
# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())
print(x.r,x.p)

#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        #%s,表示格式化一个对象为字符
        #%d,整数
        #上下两种形式类似
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
        print(str(self.name)+"说"+str(self.age)+"岁")
 
# 实例化类
p = people('runoob',10,30)
p.speak()

###########继承与派生###########
#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
#单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
s = student('ken',10,60,3)
s.speak()